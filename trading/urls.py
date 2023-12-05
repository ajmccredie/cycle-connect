from django.urls import path
from . import views
from trading.views import TradingPostView, TradingPostNewView

urlpatterns = [
    path('listings/', TradingPostView.as_view(), name='trading_list'),
    path('listings/new/', TradingPostNewView.as_view(), name='trading_new'),
]