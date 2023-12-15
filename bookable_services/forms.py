from django import forms
from .models import Service, Slot

class BookingForm(forms.Form):
    place = forms.ModelChoiceField(queryset=Place.objects.none(), required=True)
    slot = forms.ModelChoiceField(queryset=Slot.objects.none(), required=True)

    def __init__(self, *args, **kwargs):
        service_id = kwargs.pop('service_id', None)
        super().__init__(*args, **kwargs)
        if service_id:
            service = Service.objects.get(id=service_id)
            self.fields['place'].queryset = service.regions.all()
            self.fields['slot'].queryset = Slot.objects.filter(service=service, is_booked=False)
