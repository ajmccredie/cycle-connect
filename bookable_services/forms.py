from django import forms
from .models import ServiceSlot, Booking

class ServiceBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service_slot']

    def __init__(self, *args, **kwargs):
        service_id = kwargs.pop('service_id', None)
        super().__init__(*args, **kwargs)
        if service_id:
            self.fields['service_slot'].queryset = ServiceSlot.objects.filter(service_id=service_id, current_participants__lt=models.F('max_participants'))