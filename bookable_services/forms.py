from django import forms
from .models import Slot, Booking, Place, IndividualSlot

class BookingInquiryForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'place', 'individual_slot']

    place = forms.ModelChoiceField(
        queryset=Place.objects.none(), 
        label="Select Place",
        required=False
    )
    individual_slot = forms.ModelChoiceField(
        queryset=IndividualSlot.objects.none(), 
        label="Select Time Slot",
        required=False
    )

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop('service', None)
        super(BookingInquiryForm, self).__init__(*args, **kwargs)
        if self.service:
            self.fields['service'].initial = self.service
            self.fields['service'].disabled = True
            self.fields['place'].queryset = self.service.regions.all()
