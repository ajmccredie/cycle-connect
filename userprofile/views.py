from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ProfileDetails
from .forms import CustomSignupForm
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    template_name = 'userprofile/signup.html'
    form_class = CustomSignupForm


def index(request):
    # If user is authenticated, render the forum page, otherwise the sign-in page
    if request.user.is_authenticated:
        # If you have a separate forum page
        return render(request, 'userforum.html')
    else:
        # If index is your sign-in page
        return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('userforum')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def signup_full_profile(request):  
    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            profile_details = form.save(commit=False)
            profile_details.user = request.user
            profile_details.save()
            return redirect('userforum')  # Redirect to a preferred page
    else:
        form = ProfileDetailsForm()
    return render(request, 'signup_full_profile.html', {'form': form})

def profile_view(request):
    profile_details, created = ProfileDetails.objects.get(user=request.user)
    return render(request, 'profile_view.html', {'profile': profile_details})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index') 
    return render(request, 'logout_confirmation.html')
