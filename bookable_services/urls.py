from django.urls import path
from .views import BookService, ServiceList

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service_list'),
    path('bookings/<int:service_id>/', BookService.as_view(), name='book_service'),
]