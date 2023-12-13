from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Ride, RideAttendance, RideOrganiser
from .forms import RideForm

# Create your views here.
class RidesOverview(ListView, LoginRequiredMixin):
    model = Ride
    template_name = 'social_rides/rides.html'
    context_object_name = 'rides'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            registered_ride_ids = set(self.request.user.participated_rides.values_list('ride_id', flat=True))
            context['registered_ride_ids'] = registered_ride_ids
        return context


class AddRideView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = RideForm()
        return render(request, 'social_rides/add_ride.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RideForm(request.POST, request.FILES)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.organiser = request.user
            ride.save()
            return redirect('rides')
        return render(request, 'social_rides/add_ride.html', {'form': form})


class RideDetailView(DetailView, LoginRequiredMixin):
    model = Ride
    template_name = 'social_rides/ride_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ride = context['ride']
        context['registered_users'] = RideAttendance.objects.filter(ride=ride)
        return context


class RegisterForRide(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        attendance, created = RideAttendance.objects.get_or_create(ride=ride, participant=request.user)

        if not created and not attendance.is_verified: 
            attendance.delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('ride_details', kwargs={'pk': ride_id})))
