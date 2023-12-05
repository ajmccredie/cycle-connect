from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Place, Slot, Booking, Service
from .forms import BookingInquiryForm

# Create your views here.
class ServiceList(View, LoginRequiredMixin):
    model = Service
    template_name = 'service_list.html'

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services})


class SelectPlace(View):
    select_place_page = 'book_service_place.html'

    def get(self, request, service_id):
        service = get_object_or_404(Service, id=service_id)
        places = Place.objects.filter(slot__service=service).distinct()
        for place in places:
            slots = Slot.objects.filter(service=service, place=place)
            available_slots = 0
            for slot in slots:
                bookings_count = Booking.objects.filter(slot=slot).count()
                if bookings_count < slot.max_people:
                    available_slots += slot.max_people - bookings_count
            place.available_slots = available_slots
        return render(request, self.select_place_page, {'service': service, 'places': places}) 

    def post(self, request, *args, **kwargs):
        service_id = request.POST.get('service_id')
        place_id = request.POST.get('place_id')
        return redirect('book_service', service_id=service_id, place_id=place_id)


class BookService(LoginRequiredMixin, View):
    model = Booking
    service_booking_page = 'book_service.html'

    def get(self, request, service_id, place_id):
        service = get_object_or_404(Service, id=service_id)
        place = get_object_or_404(Place, id=place_id)
        current_time = timezone.now()
        slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time).order_by('start_time')
        booked_slots_ids = Booking.objects.filter(status='confirmed').values_list('slot_id', flat=True)
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
            return redirect('book_service_confirmation', booking_id=new_booking.id)
        else:
            current_time = timezone.now()
            booked_slots_ids = Booking.objects.filter(status='confirmed').values_list('slot_id', flat=True)
            available_slots = Slot.objects.filter(service=service, place=place, start_time__gte=current_time).exclude(id__in=booked_slots_ids).order_by('start_time')
            return render(request, self.service_booking_page, {'form': form, 'slots': available_slots, 'service': service, 'place': place})


def get_available_slots(request, service_id, location_id):
    try:
        service = get_object_or_404(Service, pk=service_id)
        available_slots = Slot.objects.filter(service=service, location_id=location_id)
        formatted_slots = [{'id': slot.id, 'display': str(slot)} for slot in available_slots]
        return JsonResponse({'slots': formatted_slots})
    except Service.DoesNotExist:
        return JsonResponse({'error': 'Service not found'}, status=404)


@login_required
def book_service_confirmation(request, booking_id):
    latest_booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'book_service_confirmation.html', {'booking': latest_booking})

@login_required
def booking_status(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'booking_list.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if booking.status not in ['cancelled']:
        booking.status = 'cancelled'
        booking.save()
    else:
        messages.error(request, 'Booking cannot be cancelled.')
    return redirect('booking_status')