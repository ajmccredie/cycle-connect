from django.urls import path
from .views import BookService, ServiceList, SelectPlace, BookServiceConfirmationView, BookingStatusView, CancelBookingView
from . import views

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service_list'),
    path('bookings/select_place/<int:service_id>/', SelectPlace.as_view(), name='select_place'),
    path('bookings/<int:service_id>/<int:place_id>/', BookService.as_view(), name='book_service'),
    path('bookings/confirmation/<int:booking_id>/', BookServiceConfirmationView.as_view(), name='book_service_confirmation'),
    path('bookings/status/', BookingStatusView.as_view(), name='booking_status'),
    path('bookings/cancel/<int:booking_id>/', CancelBookingView.as_view(), name='cancel_booking'),
]