from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import ProfileDetails
from ts_and_cs.models import UserVerified
from .forms import CustomSignupForm, ProfileDetailsForm
from allauth.account.views import SignupView


# Full user sign-up form
class CustomSignupView(SignupView):
    template_name = 'userprofile/signup.html'
    form_class = CustomSignupForm


# Home page for logged out and logged in users
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account_login')
        else:
            return render(request, 'index.html', {'error': 'Invalid username or password.'})


# Check login credentials
class AccountLoginView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
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


# Basic sign up form
class SignUpView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'userprofile/sign_up.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signup_full_profile')
        return render(request, 'userprofile/sign_up.html', {'form': form})


# Render full sign-up form
class SignupFullProfileView(LoginRequiredMixin, View):
    template_name = 'userprofile/signup_full_profile.html'

    def get(self, request):
        profile_details, created = ProfileDetails.objects.get_or_create(
            user=request.user,
            defaults={
                'biography': 'Please tell us a little about yourself and your cycling background',
                'cycling_skills': 'How would you describe your level of cycling expertise?',
                'preferred_ride_type': 'What type of bikes do you prefer to ride',
                'maintenance_skills': 'Tell us a little about your maintenance experience',
            }
        )
        form = ProfileDetailsForm(instance=profile_details)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        profile_details, _ = ProfileDetails.objects.get_or_create(user=request.user)
        form = ProfileDetailsForm(request.POST, request.FILES, instance=profile_details)
        if form.is_valid():
            form.save()
            user_verified, _ = UserVerified.objects.get_or_create(user=request.user)
            user_verified.profile_completed = True
            user_verified.save()
            return redirect('userforum')
        return render(request, self.template_name, {'form': form})


# View detailed profile information
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        defaults = {
            'biography': 'Please tell us a little about yourself and your cycling background',
            'cycling_skills': 'How would you describe your level of cycling expertise?',
            'preferred_ride_type': 'What type of bikes do you prefer to ride', 
            'maintenance_skills': 'Tell us a little about your maintenance experience',
        }
        profile_details, created = ProfileDetails.objects.get_or_create(user=request.user, defaults=defaults)
        return render(request, 'userprofile/profile_view.html', {'profile': profile_details})


# Edit the profile information
class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'userprofile/profile_edit.html'

    def get(self, request):
        profile_details, _ = ProfileDetails.objects.get_or_create(user=request.user)
        form = ProfileDetailsForm(instance=profile_details)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        profile_details, _ = ProfileDetails.objects.get_or_create(user=request.user)
        form = ProfileDetailsForm(request.POST, request.FILES, instance=profile_details)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
        return render(request, self.template_name, {'form': form})


# Logout from the site
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'userprofile/logout_confirmation.html')

    def post(self, request):
        logout(request)
        return redirect('index')
