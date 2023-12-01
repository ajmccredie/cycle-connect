from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.shortcuts import render
from django.http import JsonResponse
from .models import Place, Slot, Booking, Service
from .forms import BookingInquiryForm

# Create your views here.
class ServiceList(View):
    model = Service
    template_name = 'service_list.html'

    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        return render(request, self.template_name, {'services': services})


class BookService(LoginRequiredMixin, View):
    model = Booking
    service_booking_page = 'book_service.html'

    def get(self, request, *args, **kwargs):
        service_id = kwargs.get('service_id')
        service = get_object_or_404(Service, id=service_id)
        slots = Slot.objects.filter(service=service).order_by('start_time')
        form = BookingInquiryForm(initial={'service': service}, service=service)
        return render(request, self.service_booking_page, {'form': form, 'slots': slots, 'service': service})

    def post(self, request, *args, **kwargs):
        service_id = kwargs.get('pk')
        service = get_object_or_404(Service, pk=service_id)
        form = BookingInquiryForm(request.POST, service=service)
        if form.is_valid():
            new_booking = Booking(
            user=request.user,
            slot=form.cleaned_data['slot'],
            status='pending'
            )
            new_booking.save()
            return redirect('service_list')
            
        return render(request, self.service_booking_page, {'form': form})


def get_available_slots(request, service_id, location_id):
    try:
        service = get_object_or_404(Service, pk=service_id)
        available_slots = Slot.objects.filter(service=service, location_id=location_id)
        formatted_slots = [{'id': slot.id, 'display': str(slot)} for slot in available_slots]
        return JsonResponse({'slots': formatted_slots})
    except Service.DoesNotExist:
        return JsonResponse({'error': 'Service not found'}, status=404)


def book_service_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'book_service_confirmation.html', {'booking': booking})
