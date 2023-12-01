from django.urls import path
from .views import BookService, ServiceList
from . import views

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service_list'),
    path('bookings/<int:service_id>/', BookService.as_view(), name='book_service'),
    #path('bookings/<int:service_id>/<int:location_id>/', views.get_available_slots, name='available_slots'),
    path('bookings/confirmation/<int:slot_id>/', views.book_service_confirmation, name='book_service_confirmation'),
]