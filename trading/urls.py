from django.urls import path
from . import views
from trading.views import TradingPostView, TradingPostNewView, TradingPostEditView, TradingPostDeleteView
from .views import toggle_post_status

urlpatterns = [
    path('listings/', TradingPostView.as_view(), name='trading_list'),
    path('listings/new/', TradingPostNewView.as_view(), name='trading_new'),
    path('toggle-status/<int:post_id>/', toggle_post_status, name='toggle_post_status'),
    path('edit/<int:pk>/', TradingPostEditView.as_view(), name='trading_edit'),
    path('delete/<int:pk>/', TradingPostDeleteView.as_view(), name='trading_delete'),
]