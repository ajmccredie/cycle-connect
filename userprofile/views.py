from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import ProfileDetails
from .forms import CustomSignupForm
from allauth.account.views import SignupView

class CustomSignupView(SignupView):
    form_class = CustomSignupForm


def index(request):
    # If user is authenticated, render the forum page, otherwise the sign-in page
    if request.user.is_authenticated:
        # If you have a separate forum page
        return render(request, 'userprofile/forum.html')
    else:
        # If index is your sign-in page
        return render(request, 'userprofile/index.html')


def signup(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # You might want to log the user in and redirect to the index page
            return redirect('index')
    else:
        form = CustomSignUpForm()
    return render(request, 'signup.html', {'form': form})