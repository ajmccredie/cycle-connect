from django import forms
from crispy_forms.helper import FormHelper
from django.utils import timezone
from crispy_forms.layout import Layout, Submit, Field
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['title', 'date', 'image', 'route_description', 'start_place', 'end_place', 'start_time', 'distance', 'difficulty']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'difficulty': forms.RadioSelect,
        }
    
    def __init__(self, *args, **kwargs):
        super(RideForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'date',
            Field('image', template='path/to/custom_image_field.html', widget=forms.FileInput),
            'route_description',
            'start_place',
            'end_place',
            'start_time',
            'distance',
            'difficulty',
            Submit('submit', 'Create Ride', css_class='btn btn-primary')
        )
        # Remove the asterisk (*) from required fields
        for field in self.fields.values():
            field.label = ''
        for field_name, field in self.fields.items():
            field.label = field.label.strip('*')
