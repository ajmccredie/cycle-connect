from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Ride
from .forms import RideForm

# Create your views here.
class RidesOverview(ListView, LoginRequiredMixin):
    model = Ride
    template_name = 'social_rides/rides.html'
    context_object_name = 'rides'


class AddRideView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = RideForm()
        return render(request, 'social_rides/add_ride.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RideForm(request.POST, request.FILES)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.organiser = request.user
            ride.save
            return redirect('social_rides/rides.html')
        return render(request, 'social_rides/add_ride.html', {'form': form})


class RideDetailView(DetailView, LoginRequiredMixin):
    model = Ride
    template_name = 'social_rides/ride_details.html'
    context_object_name = 'ride'
