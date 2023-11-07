from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ProfileDetails
from .forms import CustomSignupForm
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

