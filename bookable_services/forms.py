from django import forms
from .models import Slot, Booking, Place

class BookingInquiryForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'place', 'date']

    place = forms.ModelChoiceField(
        queryset=Place.objects.all(), label="Select Place"
    )
    date = forms.DateField(widget=forms.SelectDateWidget(), required=False)

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop('service', None)
        super(BookingInquiryForm, self).__init__(*args, **kwargs)
        if self.service:
            self.fields['service'].initial = self.service
            self.fields['service'].disabled = True
            self.fields['date'].queryset = self.service.slot_set.values_list('start_time__date', flat=True).distinct()