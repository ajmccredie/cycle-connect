from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Ride

# Create your views here.
class RidesOverview(ListView):
    model = Ride
    template_name = 'social_rides/rides.html'
    context_object_name = 'rides'


class AddRideView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'social_rides/add_rides.html')

    def post(self, request, *args, **kwargs):
        return redirect('social_rides/rides.html')


class RideDetailView(DetailView):
    model = Ride
    template_name = 'social_rides/ride_details.html'
    context_object_name = 'ride'
