from django.shortcuts import render
from .models import Place, Slot, Booking
from .forms import BookingInquiryForm

# Create your views here.

class BookService(request):
    model = Booking
    form = BookingInquiryForm
    service_booking_page = 'services/book_service.html'
