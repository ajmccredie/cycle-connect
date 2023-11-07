from .models import ProfileDetails
from allauth.account.forms import SignupForm
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=False)


    def __init__(self, *args, **kwargs):
            super(CustomSignupForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                'first_name',
                'last_name',
                Submit('submit', 'Sign Up', css_class='btn btn-primary btn-block'),
            )

    def save(self, request):
        # Create a new user using the provided email and password
        user = super(CustomSignupForm, self).save(request)
        
        # Create a user profile associated with the user
        user.profile.first_name = self.cleaned_data['first_name']
        user.profile.last_name = self.cleaned_data['last_name']
        user.profile.save()

        return user