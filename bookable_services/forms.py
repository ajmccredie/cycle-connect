from django import forms
from .models import Slot, Booking, Place

class BookingInquiryForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'place', 'slot']

    place = forms.ModelChoiceField(
        queryset=Place.objects.all(), label="Select Place"
    )
    date = forms.DateField(widget=forms.SelectDateWidget(), required=False)

    def __init__(self, *args, **kwargs):
        super(BookingInquiryForm, self).__init__(*args, **kwargs)
        self.fields['slot'].queryset = Slot.objects.none()
        if 'place' in self.data and 'date' in self.data:
            try:
                place_id = int(self.data.get('place'))
                date = self.data.get('date')
                self.fields['slot'].queryset = Slot.objects.filter(place_id=place_id, start_time__date=date)
            except (ValueError, TypeError):
                pass

