from django.shortcuts import render
from .models import Place, Slot, Booking
from .forms import BookingInquiryForm

# Create your views here.

def book_service(request):
    
