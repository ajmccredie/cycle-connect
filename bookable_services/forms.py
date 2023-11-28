from django import forms
from .models import Slot, Booking

class BookingInquiryForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['slot', 'user']