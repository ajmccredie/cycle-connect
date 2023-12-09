from django.shortcuts import redirect
from django.urls import reverse
from .models import UserVerified

class TermsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated and not request.path.startswith(reverse('terms_and_conditions')):
            user_verified, created = UserVerified.objects.get_or_create(user=request.user)
            if not user_verified.agreed_to_terms:
                return redirect(reverse('terms_and_conditions'))
        return response
