from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserVerified

# Terms and conditions page
class TermsAndConditionsView(LoginRequiredMixin, View):
    template_name = 'ts_and_cs/terms.html'

    def get(self, request, *args, **kwargs):
        user_verified, created = UserVerified.objects.get_or_create(user=request.user)
        if user_verified.agreed_to_terms:
            if not user_verified.profile_completed:
                return redirect('signup_full_profile')  # Redirect to complete profile
            return redirect('index')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        user_verified, created = UserVerified.objects.get_or_create(user=request.user)
        user_verified.agreed_to_terms = True
        user_verified.save()
        if not user_verified.profile_completed:
            return redirect('signup_full_profile')  # Redirect to complete profile
        return redirect('index')


# Custom 404 page
def custom_404(request, exception):
    return render(request, 'ts_and_cs/custom_404.html', {}, status=404)


# Custom 500 page
def custom_500_handler(request):
    return render(request, 'ts_and_cs/custom_500.html', status=500)