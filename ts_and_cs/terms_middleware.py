from django.shortcuts import redirect
from django.urls import reverse

class TermsMiddleware:
    def __init__(self, get_reponse):
        self.get_reponse = get_reponse

    def __call__(self, request):
        response = self.get_reponse(request)
        if request.user.is_authenticated and not request.user.agreed_to_terms:
            return redirect(reverse('terms_and_conditions'))
        return response