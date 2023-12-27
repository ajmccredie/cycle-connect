from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from datetime import datetime
from .models import Ride, RideAttendance, RideOrganiser
from .forms import RideForm

# View all the rides
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
            verified_attendance_count = RideAttendance.objects.filter(participant=self.request.user, is_verified=True).count()
            context['verified_attendance_count'] = verified_attendance_count
        return context


# Add a new ride
class AddRideView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = RideForm()
        current_date = timezone.now().date().isoformat()
        is_trusted_organiser = RideOrganiser.objects.filter(user=request.user, trusted_organiser=True).exists()
        return render(request, 'social_rides/add_ride.html', {'form': form, 'current_date': current_date, 'is_trusted_organiser': is_trusted_organiser})

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


# View ride details
class RideDetailView(DetailView, LoginRequiredMixin):
    model = Ride
    template_name = 'social_rides/ride_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ride = self.get_object()
        now = timezone.now()

        local_timezone = timezone.get_current_timezone()
        combined_datetime = local_timezone.localize(datetime.combine(ride.date, ride.start_time))
        is_past_ride = combined_datetime < now
        context['is_past_ride'] = is_past_ride
        registered_count = ride.attendees.count()
        context['available_spaces'] = ride.max_participants - registered_count
        context['is_full'] = context['available_spaces'] <= 0
        context['current_date'] = now.date()
        context['current_time'] = now
        combined_datetime = datetime.combine(ride.date, ride.start_time)
        context['combined_datetime'] = combined_datetime
        if self.request.user.is_authenticated:
            user_is_registered = RideAttendance.objects.filter(ride=ride, participant=self.request.user).exists()
            context['is_user_registered'] = user_is_registered
            context['registered_users'] = RideAttendance.objects.filter(ride=ride)
        context['is_organiser'] = ride.organiser == self.request.user
        return context


# Register attendance
class RegisterForRide(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        attendance, created = RideAttendance.objects.get_or_create(ride=ride, participant=request.user)

        if not created and not attendance.is_verified: 
            attendance.delete()
        return redirect('ride_details', pk=ride_id)


# Edit unverified rides
class RideEditView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user:
            messages.error(request, "You are not authorised to edit this ride.")
            return redirect('ride_details', pk=ride_id)
        current_date = timezone.now().date().isoformat()
        if ride.attendees.count() == 0 and not ride.is_verified:
            form = RideForm(instance=ride)
            return render(request, 'social_rides/edit_ride.html', {'form': form, 'ride': ride, 'current_date': current_date})
        else:
            messages.error(request, "This ride cannot be edited.")
            return redirect('ride_details', pk=ride_id)

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user:
            messages.error(request, "You are not authorised to edit this ride.")
            return redirect('ride_details', pk=ride_id)
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



# Confirm delete of unverified rides
class RideConfirmDeleteView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user:
            messages.error(request, "You are not authorised to delete this ride.")
            return redirect('rides')
        return render(request, 'social_rides/confirm_delete_ride.html', {'ride': ride})


# Delete unverified rides
class RideDeleteView(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user:
            messages.error(request, "You are not authorised to delete this ride.")
            return redirect('rides')
        if ride.attendees.count() == 0 and not ride.is_verified:
            ride.delete()
            messages.success(request, "Ride successfully deleted.")
        else:
            messages.error(request, "This ride cannot be deleted.")
        return redirect('rides')


# Confirm cancel rides
class RideConfirmCancelView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user:
            messages.error(request, "You are not authorised to cancel this ride.")
            return redirect('ride_details', pk=ride_id)
        return render(request, 'social_rides/confirm_cancel_ride.html', {'ride': ride})


# Cancel rides
class RideCancelView(LoginRequiredMixin, View):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.organiser != request.user:
            messages.error(request, "You are not authorised to cancel this ride.")
            return redirect('rides')
        ride.is_cancelled = True
        ride.save()
        messages.success(request, "Ride has been cancelled.")
        return redirect('ride_details', pk=ride_id)


# Verify attendance
class VerifyAttendanceView(LoginRequiredMixin, View):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        local_timezone = timezone.get_current_timezone()
        combined_datetime = local_timezone.localize(datetime.combine(ride.date, ride.start_time))
        now = timezone.now()
        if ride.organiser != request.user or now <= combined_datetime:
            return redirect('ride_details', pk=ride_id)
        attendees = RideAttendance.objects.filter(ride=ride)
        return render(request, 'social_rides/verify_attendance.html', {'ride': ride, 'attendees': attendees})

    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        naive_combined_datetime = datetime.combine(ride.date, ride.start_time)
        combined_datetime = timezone.make_aware(naive_combined_datetime, timezone.get_default_timezone())
        if ride.organiser != request.user or timezone.now() <= combined_datetime:
            return redirect('ride_details', pk=ride_id)

        for key, value in request.POST.items():
            if key.startswith('verify_'):
                attendance_id = key.split('_')[1]
                attendance_record = RideAttendance.objects.get(id=attendance_id)
                attendance_record.is_verified = value == 'on'
                attendance_record.save()

        return redirect('ride_details', pk=ride_id)
