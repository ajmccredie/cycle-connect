from django import forms
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError
from django.utils import timezone
from crispy_forms.layout import Layout, Submit, Field
from .models import Ride

# Set up form for new rides
class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['title', 'date', 'image', 'route_description', 'start_place', 'end_place', 'start_time', 'distance', 'difficulty']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'difficulty': forms.RadioSelect,
        }
    
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        route_description = cleaned_data.get('route_description')
        if date and start_time:
            now = timezone.localtime(timezone.now())
            ride_datetime = timezone.make_aware(timezone.datetime.combine(date, start_time))
            if ride_datetime < now:
                raise ValidationError('You cannot organize a ride in the past.')
        if route_description and len(route_description) > 750:
            self.add_error('route_description', 'Route description cannot be longer than 750 characters.')
        return cleaned_data

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            max_size = 9 * 1024 * 1024  # 9MB
            if image.size > max_size:
                raise ValidationError('Image file too large ( > 9MB )')
        return image
    
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
