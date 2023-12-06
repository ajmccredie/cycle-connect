from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.views import generic, View
from django.views.generic import ListView
from .models import TradingPost, TradingConversation
from .forms import TradingPostForm
from django.contrib import messages

# Create your views here.

class TradingPostView(ListView, LoginRequiredMixin):
    model = TradingPost
    template_name = 'trading/trading_list.html'
    paginate_by = 6
    context_object_name = 'trading_posts'

    def get_queryset(self):
        user = self.request.user
        queryset = TradingPost.objects.filter(Q(approved=1) | Q(seller=user))

        category = self.request.GET.get('category')
        condition = self.request.GET.get('condition')

        if category:
            queryset = queryset.filter(category=category)
        if condition:
            queryset = queryset.filter(condition=condition)
        return queryset.order_by('-created_on')

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
            messages.success(request, 'New post created successfully!')
            return redirect('trading_list')
        return render(request, self.template_name, {'form': form}) 


class TradingPostEditView(View, LoginRequiredMixin):
    template_name = 'trading/trading_edit.html'
    
    def get(self, request, pk):
        post = get_object_or_404(TradingPost, pk=pk, seller=request.user)
        form = TradingPostForm(instance=post)
        return render(request, self.template_name, {'form': form})
    
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


class TradingConversationView(View, LoginRequiredMixin):
    def post(self, request, post_id):
        post = get_object_or_404(TradingPost, pk=post_id)
        if request.user != post.seller:
            TradingConversation.objects.get_or_create(
                post=post,
                seller=post.seller,
                buyer=request.user
            )
        return redirect('trading_list')
