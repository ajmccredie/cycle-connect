from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.shortcuts import render
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
        form = BookingInquiryForm()
        return render(request, self.service_booking_page, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BookingInquiryForm(request.POST)
        if form.is_valid():
            new_booking = Booking(
                user=request.user,
                slot=form.cleaned_data['slot'],
                status='pending'
            )
            new_booking.save()
            
        return render(request, self.service_booking_page, {'form': form})