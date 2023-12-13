from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Ride
from .forms import RideForm

# Create your views here.
class RidesOverview(ListView):
    model = Ride
    template_name = 'social_rides/rides.html'
    context_object_name = 'rides'


class AddRideView(View):
    def get(self, request, *args, **kwargs):
        form = RideForm()
        return render(request, 'social_rides/add_rides.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('social_rides/rides.html')
        return render(request, 'social_rides/add_rides.html', {'form': form})


class RideDetailView(DetailView):
    model = Ride
    template_name = 'social_rides/ride_details.html'
    context_object_name = 'ride'
