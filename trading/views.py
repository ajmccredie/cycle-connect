from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from .models import TradingPost
from .forms import TradingPostForm

# Create your views here.

class TradingPostView(ListView, LoginRequiredMixin):
    model = TradingPost
    template_name = 'trading/trading_list.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = TradingPost.objects.filter(approved=1)
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


class TradingPostNewView(View, LoginRequiredMixin):
    form_class = TradingPostForm
    template_name = 'trading/trading_new.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            trading_post = form.save(commit=False)
            trading_post.user = request.user
            trading_post.save()
            messages.success(request, 'New post created successfully!')
            return redirect('trading_list')
        return render(request, self.template_name, {'form': form}) 

