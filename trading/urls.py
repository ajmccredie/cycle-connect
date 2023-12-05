from django.urls import path
from . import views
from trading.views import TradingPostView

urlpatterns = [
    path('listings/', TradingPostView.as_view(), name='trading_list'),
]