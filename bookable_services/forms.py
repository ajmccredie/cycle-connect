from django import forms
from .models import Slot, Booking, Place

class BookingInquiryForm(forms.ModelForm):
    place = forms.ModelChoiceField(
        queryset=Place.objects.all(),
    )
    date = forms.DateField(widget=forms.Select(attrs={'disabled': 'true'}))
    time_slot = forms.ModelChoiceField(
        queryset=Slot.objects.none(),
    )

    