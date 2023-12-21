from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from .models import Place, Slot, Booking, Service
from .forms import BookingInquiryForm

# Create your views here.
# This allows the services available all to be seen on the main page
class ServiceList(View, LoginRequiredMixin):
    model = Service
    template_name = 'services/service_list.html'
    
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services})


# The user then selects the place they want the service to occur from any that are available
class SelectPlace(View):
    select_place_page = 'services/book_service_place.html'
    
    def get(self, request, service_id):
        service = get_object_or_404(Service, id=service_id)
        current_time = timezone.now()
        places = Place.objects.filter(slot__service=service, slot__start_time__gte=current_time).distinct()
        places_slots_info = {}
        for place in places:
            slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time)
            for slot in slots:
                slot.update_status()
            available_slots_count = slots.filter(status='available').count()
            places_slots_info[place.id] = available_slots_count
        return render(request, self.select_place_page, {'service': service, 'places': places, 'places_slots_info': places_slots_info})
    # def post(self, request, *args, **kwargs):
    #     service_id = request.POST.get('service_id')
    #     place_id = request.POST.get('place_id')
    #     return redirect('services/book_service', service_id=service_id, place_id=place_id)


# User then selects the date and time-slot they want to book for the service they want in the place they have chosen
class BookService(LoginRequiredMixin, View):
    model = Booking
    service_booking_page = 'services/book_service.html'
    
    def get(self, request, service_id, place_id):
        service = get_object_or_404(Service, id=service_id)
        place = get_object_or_404(Place, id=place_id)
        current_time = timezone.now()
        slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time).order_by('start_time')
        booked_slots_ids = Booking.objects.filter(status__in=['confirmed', 'pending']).values_list('slot_id', flat=True)
        available_slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time).exclude(id__in=booked_slots_ids).order_by('start_time')
        form = BookingInquiryForm(initial={'service': service}, service=service)
        return render(request, self.service_booking_page, {'form': form, 'slots': available_slots, 'service': service, 'place': place})

    def post(self, request, service_id, place_id):
        slot_id = request.POST.get('slot_id')
        service = get_object_or_404(Service, id=service_id)
        place = get_object_or_404(Place, id=place_id)
        form = BookingInquiryForm(request.POST, service=service)
        
        if slot_id:
            slot = get_object_or_404(Slot, id=slot_id)
            service = get_object_or_404(Service, id=service_id)
            new_booking = Booking.objects.create(
                user=request.user,
                slot=slot,
                service=service,
                status='pending'
            )
            slot.update_status()
            return redirect('book_service_confirmation', booking_id=new_booking.id)
        else:
            current_time = timezone.now()
            booked_slots_ids = Booking.objects.filter(status='confirmed').values_list('slot_id', flat=True)
            available_slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time).exclude(id__in=booked_slots_ids).order_by('start_time')
            return render(request, self.service_booking_page, {'form': form, 'slots': available_slots, 'service': service, 'place': place})


# Receipt of confirmation of booking
class BookServiceConfirmationView(LoginRequiredMixin, View):
    def get(self, request, booking_id):
        latest_booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        return render(request, 'services/book_service_confirmation.html', {'booking': latest_booking})


# Users can view the status of any bookings they have made and have the option to cancel
class BookingStatusView(LoginRequiredMixin, View):
    def get(self, request):
        current_time = timezone.now()
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
        for booking in bookings:
            booking.is_past = booking.booking_date < current_time
        return render(request, 'services/booking_list.html', {'bookings': bookings})


# Users can cancel their bookings
class CancelBookingView(LoginRequiredMixin, View):
    @method_decorator(require_http_methods(["POST"]))
    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        if booking.status != 'cancelled':
            booking.status = 'cancelled'
            booking.save()
            messages.success(request, 'Booking cancelled successfully.')
        else:
            messages.error(request, 'Booking cannot be cancelled.')
        return redirect('booking_status') 