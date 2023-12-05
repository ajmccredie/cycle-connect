from django.shortcuts import render
from django.views.generic import ListView
from .models import TradingPost
from .form import TradingPostForm

# Create your views here.

class TradingPostView(ListView):
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


