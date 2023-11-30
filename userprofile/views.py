from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ProfileDetails
from .forms import CustomSignupForm, ProfileDetailsForm
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    template_name = 'userprofile/signup.html'
    form_class = CustomSignupForm


def index(request):
    # If user is authenticated, render the forum page, otherwise the sign-in page
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account_login')
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password.'})
    else:
        return render(request, 'index.html')


def account_login(request):
    if request.method == 'POST':
        # Retrieve username and password from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userforum')
        else:
            return render(request, 'index.html', {
                'error': 'Invalid username or password. Please try again.'
            })
    else:
        return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup_full_profile')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

@login_required
def signup_full_profile(request):
    user = request.user
    defaults = {
        'biography': 'Please tell us a little about yourself and your cycling background',
        'cycling_skills': 'How would you describe your level of cycling expertise?',
        'preferred_ride_type': 'What type of bikes do you prefer to ride', 
        'maintenance_skills': 'Tell us a little about your maintenance experience',
    }
    profile_details, created = ProfileDetails.objects.get_or_create(user=user, defaults=defaults)  
    
    try:
        profile_details = ProfileDetails.objects.get(user=request.user)
    except ProfileDetails.DoesNotExist:
        profile_details = None
    
    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, request.FILES, instance=profile_details)
        if form.is_valid():
            profile_details = form.save(commit=False)
            profile_details.user = request.user
            profile_details.save()
            return redirect('userforum')
    else:
         form = ProfileDetailsForm(instance=profile_details if profile_details else None)

    return render(request, 'signup_full_profile.html', {'form': form})


@login_required
def profile_view(request):
    defaults = {
        'biography': 'Please tell us a little about yourself and your cycling background',
        'cycling_skills': 'How would you describe your level of cycling expertise?',
        'preferred_ride_type': 'What type of bikes do you prefer to ride', 
        'maintenance_skills': 'Tell us a little about your maintenance experience',
    }
    profile_details, created = ProfileDetails.objects.get_or_create(user=request.user, defaults=defaults)
    return render(request, 'profile_view.html', {'profile': profile_details})


def profile_edit(request):
    user = request.user
    try:
        profile_details = ProfileDetails.objects.get(user=user)
    except ProfileDetails.DoesNotExist:
        profile_details = None

    if request.method == 'POST':
        form = ProfileDetailsForm(request.POST, request.FILES, instance=profile_details)
        if form.is_valid():
            preferred_ride_type_values = form.cleaned_data.get('preferred_ride_type')
            print("Preferred Ride Type values submitted:", preferred_ride_type_values)
            form.save()
            return redirect('profile_view')
        else:
            print("Form errors", form.errors)
    else:
        form = ProfileDetailsForm(instance=profile_details)
    return render(request, 'profile_edit.html', {'form': form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index') 
    return render(request, 'logout_confirmation.html')
