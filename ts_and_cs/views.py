from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserVerified

# Create your views here.
class TermsAndConditionsView(LoginRequiredMixin, View):
    template_name = 'ts_and_cs/terms.html'

    def get(self, request, *args, **kwargs):
        if request.user.agreed_to_terms:
            return redirect('index.html')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        request.user.agreed_to_terms = True
        request.user.save()
        return redirect('index.html')
