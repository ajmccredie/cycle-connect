from django.urls import path
from .views import RidesOverview, RideDetailView, AddRideView, RegisterForRide
from . import views

urlpatterns = [
    path('rides/', RidesOverview.as_view(), name='rides'),
    path('add_ride/', AddRideView.as_view(), name='add_ride'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride_details'),
    path('ride/<int:ride_id>/register/', views.RegisterForRide.as_view(), name='register_for_ride'),
]
