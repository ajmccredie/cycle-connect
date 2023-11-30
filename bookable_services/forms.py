from django import forms
from .models import Slot, Booking, Place

class BookingInquiryForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['slot', 'service']

    place = forms.ModelChoiceField(
        queryset=Place.objects.all(), label="Select Place"
    )
    date = forms.DateField(widget=forms.Select(attrs={'disabled': 'true'}))
    time_slot = forms.ModelChoiceField(
        queryset=Slot.objects.none(), label="Select Plot"
    )

    def __init__(self, *args, **kwargs):
        super(BookingInquiryForm, self).__init__(*args, **kwargs)
        if 'place' in self.data:
            try:
                place_id = int(self.data.get('place'))
                self.fields['slot'].queryset = Slot.objects.filter(place_id=place_id)
            except (ValueError, TypeError):
                pass

