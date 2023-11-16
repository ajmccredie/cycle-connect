from .models import ProfileDetails
from allauth.account.forms import SignupForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django import forms


class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='First Name', required=True)

    

    def __init__(self, *args, **kwargs):
            super(CustomSignupForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                'username',
                Submit('submit', 'Sign Up', css_class='btn btn-primary btn-block'),
            )

    def save(self, request):
        # Create a new user using the provided email and password
        userprofile = super(CustomSignupForm, self).save(request)
        
        # Create a user profile associated with the user
        userprofile.profile.username = self.cleaned_data['username']
        userprofile.profile.save()

        return userprofile