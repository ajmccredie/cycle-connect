from .models import ProfileDetails
from allauth.account.forms import SignupForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django import forms


class CustomSignupForm(SignupForm):
    PREFERRED_RIDE_TYPE_CHOICES = [
    ("road", "Road"),
    ("electric", "Electric"),
    ("bmx", "BMX"),
    ("mountain", "Mountain"),
    ("hybrid", "Hybrid"),
    ]
    biography = forms.CharField(required=False, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput)
    cycling_skills = forms.ChoiceField(required=False, choices=[("beginner", "Beginner"), ("casual", "Casual"), ("intermediate", "Intermediate"), ("advanced", "Advanced")], widget=forms.RadioSelect)
    preferred_ride_type = forms.ChoiceField(required=False, choices=PREFERRED_RIDE_TYPE_CHOICES, widget=forms.RadioSelect)
    maintenance_skills = forms.ChoiceField(required=False, choices=[("none", "None"), ("casual", "Casual"), ("basic", "Basic"), ("advanced", "Advanced"), ("youtube_is_my_hero", "YouTube is my hero!")], widget=forms.RadioSelect)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        profile_details, created = ProfileDetails.objects.get_or_create(user=user)
        profile_details = ProfileDetails(
            biography=self.cleaned_data['biography'],
            profile_picture=self.cleaned_data['profile_picture'],
            cycling_skills=self.cleaned_data['cycling_skills'],
            preferred_ride_type=self.cleaned_data['preferred_ride_type'],
            maintenance_skills=self.cleaned_data['maintenance_skills']
        )
        profile_details.save()
        return user


class ProfileDetailsForm(forms.ModelForm):
    PREFERRED_RIDE_TYPE_CHOICES = [
    ("road", "Road"),
    ("electric", "Electric"),
    ("bmx", "BMX"),
    ("mountain", "Mountain"),
    ("hybrid", "Hybrid"),
    ]

    biography = forms.CharField(required=False, widget=forms.Textarea)
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput)
    cycling_skills = forms.ChoiceField(required=False, choices=[("beginner", "Beginner"), ("casual", "Casual"), ("intermediate", "Intermediate"), ("advanced", "Advanced")], widget=forms.RadioSelect)
    preferred_ride_type = forms.ChoiceField(required=False, choices=PREFERRED_RIDE_TYPE_CHOICES, widget=forms.RadioSelect)
    maintenance_skills = forms.ChoiceField(required=False, choices=[("none", "None"), ("casual", "Casual"), ("basic", "Basic"), ("advanced", "Advanced"), ("youtube_is_my_hero", "YouTube is my hero!")], widget=forms.RadioSelect)
    
    class Meta:
        model = ProfileDetails
        fields = ['biography', 'profile_picture', 'cycling_skills', 'preferred_ride_type', 'maintenance_skills']

    def __init__(self, *args, **kwargs):
        super(ProfileDetailsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'biography',
            'profile_picture',
            'cycling_skills',
            'preferred_ride_type',
            'maintenance_skills',
            Submit('submit', 'Save Changes', css_class='btn btn-submit')
        )

