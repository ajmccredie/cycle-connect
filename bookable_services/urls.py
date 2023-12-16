# from django.urls import path
# from .views import ServiceListView

# urlpatterns = [
#     path('services/', ServiceListView.as_view(), name='service_list'),
# #     path('bookings/select_place/<int:service_id>/', SelectPlace.as_view(), name='select_place'),
# #    # path('bookings/<int:service_id>/<int:place_id>/', BookService.as_view(), name='book_service'),
# #    # path('bookings/confirmation/<int:booking_id>/', views.book_service_confirmation, name='book_service_confirmation'),
# #    # path('bookings/status/', booking_status, name='booking_status'),
# #    # path('bookings/cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
# ]

from django.urls import path
from .views import BookService, ServiceList, SelectPlace, book_service_confirmation, booking_status, cancel_booking
from . import views

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service_list'),
    path('bookings/select_place/<int:service_id>/', SelectPlace.as_view(), name='select_place'),
    path('bookings/<int:service_id>/<int:place_id>/', BookService.as_view(), name='book_service'),
    path('bookings/confirmation/<int:booking_id>/', views.book_service_confirmation, name='book_service_confirmation'),
    path('bookings/status/', booking_status, name='booking_status'),
    path('bookings/cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
]