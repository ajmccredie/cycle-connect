from django.urls import path
from .views import TermsAndConditionsView

urlpatterns = [
    path('terms/', TermsAndConditionsView.as_view(), name='terms_and_conditions')
]