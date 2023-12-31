from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, Subquery, OuterRef, Case, When, Value, IntegerField
from django.views import View
from django.views.generic import ListView
from .models import TradingPost, TradingConversation, Message
from .forms import TradingPostForm, MessageForm
from django.contrib import messages


# Display listings
class TradingPostView(ListView, LoginRequiredMixin):
    model = TradingPost
    template_name = 'trading/trading_list.html'
    paginate_by = 6
    context_object_name = 'trading_posts'

    def get_queryset(self):
        user = self.request.user
        queryset = TradingPost.objects.filter(Q(approved=1) | Q(seller=user))

        # Category and condition filtering
        category = self.request.GET.get('category')
        condition = self.request.GET.get('condition')
        if category:
            queryset = queryset.filter(category=category)
        if condition:
            queryset = queryset.filter(condition=condition)
        
        # Sold status filtering
        queryset = queryset.annotate(
            is_sold=Case(
                When(status='sold', then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        )

        # Determine and diplay conversation count
        queryset = queryset.annotate(conversation_count=Count('conversations'))
        user_conversation_subquery = TradingConversation.objects.filter(
            post=OuterRef('pk'), 
            buyer=user
        ).order_by('-created_at').values('id')[:1]
        queryset = queryset.annotate(user_conversation_id=Subquery(user_conversation_subquery))

        return queryset.order_by('is_sold', '-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = TradingPost.CATEGORY_CHOICES
        context['conditions'] = TradingPost.CONDITION_CHOICES
        return context


@require_POST
def toggle_post_status(request, post_id):
    post = get_object_or_404(TradingPost, id=post_id, seller=request.user)
    post.status = 'sold' if post.status == 'available' else 'available'
    post.save()
    return redirect('trading_list')


# Add new items
class TradingPostNewView(View, LoginRequiredMixin):
    form_class = TradingPostForm
    template_name = 'trading/trading_new.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user_is_authenticated:
            queryset = queryset.filter(Q(approved=1) | Q(seller=self.request.user))

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            trading_post = form.save(commit=False)
            trading_post.seller = request.user
            trading_post.save()
            messages.warning(request, 'New trading post')
            return redirect('trading_list')
        return render(request, self.template_name, {'form': form}) 


# Edit existing items
class TradingPostEditView(View, LoginRequiredMixin):
    template_name = 'trading/trading_edit.html'
    
    def get(self, request, pk):
        post = get_object_or_404(TradingPost, pk=pk, seller=request.user)
        form = TradingPostForm(instance=post)
        image_url = post.image.url if post.image else None
        return render(request, self.template_name, {'form': form, 'image_url':image_url})
    
    def post(self, request, pk):
        post = get_object_or_404(TradingPost, pk=pk, seller=request.user)
        form = TradingPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('trading_list')
        return render(request, self.template_name, {'form': form})
    
    def test_func(self):
        post = get_object_or_404(TradingPost, pk=self.kwargs['pk'])
        return self.request.user == post.seller


# Delete existing post
class TradingPostDeleteView(View, LoginRequiredMixin):
    template_name = 'trading/trading_delete.html'

    def get(self, request, pk):
        post = get_object_or_404(TradingPost, pk=pk, seller=request.user)
        return render(request, self.template_name, {'post': post})
    
    def post(self, request, pk):
        post = get_object_or_404(TradingPost, pk=pk, seller=request.user)
        post.delete()
        return redirect('trading_list')
    
    def test_func(self):
        post = get_object_or_404(TradingPost, pk=self.kwargs['pk'])
        return self.request.user == post.seller


# Discuss posts
class TradingConversationView(View, LoginRequiredMixin):
    model = TradingConversation
    template_name = 'trading/trading_conversation.html'

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        for post in queryset:
            post.has_conversation = TradingConversation.objects.filter(post=post, buyer=user).exists()
        return queryset

    def get(self, request, post_id=None, conversation_id=None):
        conversation = None
        messages = None
        if conversation_id:
            conversation = get_object_or_404(TradingConversation, id=conversation_id)
            if request.user not in [conversation.buyer, conversation.seller]:
                return redirect('trading_list') 
            messages = Message.objects.filter(conversation=conversation).order_by('created_at')
        elif post_id:
            post = get_object_or_404(TradingPost, pk=post_id)
            if request.user != post.seller:
                conversation, created = TradingConversation.objects.get_or_create(
                    post=post,
                    seller=post.seller,
                    buyer=request.user
                )
                messages = Message.objects.filter(conversation=conversation).order_by('created_at')
        form = MessageForm()
        return render(request, self.template_name, {
            'form': form,
            'conversation': conversation,
            'messages': messages,
            'post_id': post_id
        })

    def post(self, request, conversation_id=None):
        if conversation_id:
            conversation = get_object_or_404(TradingConversation, id=conversation_id)
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.conversation = conversation
                message.sender = request.user
                message.save()
                return redirect('view_conversation', conversation_id=conversation_id)
        else:
            post_id = request.POST.get('post_id')        
            post = get_object_or_404(TradingPost, pk=post_id)
            if request.user != post.seller:
                conversation, created = TradingConversation.objects.get_or_create(
                    post=post,
                    seller=post.seller,
                    buyer=request.user
                )
                return redirect('view_conversation', conversation_id=conversation.id)
        return redirect('trading_list')
