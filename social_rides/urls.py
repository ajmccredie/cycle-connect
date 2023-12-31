from django.urls import path
from .views import RidesOverview, RideDetailView, AddRideView, RegisterForRide, RideEditView, RideDeleteView, RideCancelView, RideConfirmDeleteView, RideConfirmCancelView, VerifyAttendanceView
from . import views

urlpatterns = [
    path('rides/', RidesOverview.as_view(), name='rides'),
    path('add_ride/', AddRideView.as_view(), name='add_ride'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride_details'),
    path('ride/<int:ride_id>/register/', views.RegisterForRide.as_view(), name='register_for_ride'),
    path('ride/<int:ride_id>/edit_ride/', views.RideEditView.as_view(), name='edit_ride'),
    path('ride/<int:ride_id>/delete_ride/', views.RideDeleteView.as_view(), name='delete_ride'),
    path('ride/<int:ride_id>/confirm_delete/', views.RideConfirmDeleteView.as_view(), name='confirm_delete_ride'),
    path('ride/<int:ride_id>/cancel_ride/', views.RideCancelView.as_view(), name='cancel_ride'),
    path('ride/<int:ride_id>/confirm_cancel/', views.RideConfirmCancelView.as_view(), name='confirm_cancel_ride'),
    path('ride/<int:ride_id>/verify_attendance/', VerifyAttendanceView.as_view(), name='verify_attendance'),
]
