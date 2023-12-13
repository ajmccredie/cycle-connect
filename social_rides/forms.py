from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['title', 'date', 'image', 'route_description', 'start_place', 'end_place', 'start_time', 'distance', 'difficulty']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
        }