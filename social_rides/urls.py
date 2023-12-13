from django.urls import path
from .views import RidesOverview, RideDetailView, AddRideView

urlpatterns = [
    path('rides/', RidesOverview.as_view(), name='rides'),
    path('add/', AddRideView.as_view(), name='add_ride'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride'),
]