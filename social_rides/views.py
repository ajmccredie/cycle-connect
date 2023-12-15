from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q, ExpressionWrapper, DateTimeField
from django.db.models.functions import Coalesce
from django.utils import timezone
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
        now = timezone.now()
        base_query = Ride.objects.filter(Q(is_verified=True) | Q(organiser=self.request.user))
        context['upcoming_rides'] = base_query.filter(
            Q(date__gt=now.date()) | Q(date=now.date(), start_time__gte=now.time())
        ).order_by('date', 'start_time')
        context['past_rides'] = base_query.filter(
            Q(date__lt=now.date()) | Q(date=now.date(), start_time__lt=now.time())
        ).order_by('-date', '-start_time')
        for ride in context['upcoming_rides']:
            spaces_left = max(ride.max_participants - ride.attendees.count(), 0)
            ride.spaces_left = 'Full' if spaces_left == 0 else spaces_left
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
            if RideOrganiser.objects.filter(user=request.user, trusted_organiser=True).exists():
                ride.is_verified = True
            ride.save()
            return redirect('rides')
        return render(request, 'social_rides/add_ride.html', {'form': form})


class RideDetailView(DetailView, LoginRequiredMixin):
    model = Ride
    template_name = 'social_rides/ride_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ride = self.get_object()
        registered_count = ride.attendees.count()
        context['available_spaces'] = ride.max_participants - registered_count
        context['is_full'] = context['available_spaces'] <= 0
        context['current_date'] = timezone.now().date()
        context['current_time'] = timezone.now()
        if self.request.user.is_authenticated:
            context['is_user_registered'] = RideAttendance.objects.filter(ride=ride, participant=self.request.user).exists()
            context['registered_users'] = RideAttendance.objects.filter(ride=ride)
        return context


class RegisterForRide(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        attendance, created = RideAttendance.objects.get_or_create(ride=ride, participant=request.user)

        if not created and not attendance.is_verified: 
            attendance.delete()
        return redirect('ride_details', pk=ride_id)


class RideEditView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id, organiser=request.user)
        if ride.attendees.count() == 0 and not ride.is_verified:
            form = RideForm(instance=ride)
            return render(request, 'social_rides/edit_ride.html', {'form': form, 'ride': ride})
        else:
            messages.error(request, "This ride cannot be edited.")
            return redirect('ride_details', pk=ride_id)

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id, organiser=request.user)
        if ride.attendees.count() == 0 and not ride.is_verified:
            form = RideForm(request.POST, instance=ride)
            if form.is_valid():
                form.save()
                messages.success(request, "Ride successfully updated.")
                return redirect('ride_details', pk=ride_id)
            else:
                return render(request, 'social_rides/edit_ride.html', {'form': form, 'ride': ride})
        else:
            messages.error(request, "This ride cannot be edited.")
            return redirect('ride_details', pk=ride_id)


class RideConfirmDeleteView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id, organiser=request.user)
        return render(request, 'social_rides/confirm_delete_ride.html', {'ride': ride})


class RideDeleteView(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id, organiser=request.user)
        if ride.attendees.count() == 0 and not ride.is_verified:
            ride.delete()
            messages.success(request, "Ride successfully deleted.")
        else:
            messages.error(request, "This ride cannot be deleted.")
        return redirect('rides')


class RideConfirmCancelView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id, organiser=request.user)
        return render(request, 'social_rides/confirm_cancel_ride.html', {'ride': ride})


class RideCancelView(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id, organiser=request.user)
        ride.is_cancelled = True
        ride.save()
        messages.success(request, "Ride has been cancelled.")
        return redirect('ride_details', pk=ride_id)


class VerifyAttendanceView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user or timezone.now() <= ride.start_time:
            return redirect('ride_details')
        attendees = RideAttendance.objects.filter(ride=ride)
        return render(request, 'verify_attendance.html', {'ride': ride, 'attendees': attendees})

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user or timezone.now() <= ride.combined_datetime:
            return redirect('ride_details')

        for key, value in request.POST.items():
            if key.startswith('verify_'):
                attendance_id = key.split('_')[1]
                attendance_record = RideAttendance.objects.get(id=attendance_id)
                attendance_record.is_verified = value == 'on'
                attendance_record.save()

        return redirect('ride_details')
