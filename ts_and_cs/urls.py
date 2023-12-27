from django.urls import path
from .views import TermsAndConditionsView
from ts_and_cs.views import custom_404, custom_500_handler

handler500 = 'ts_and_cs.views.custom_500_handler'
handler404 = 'ts_and_cs.views.custom_404'

urlpatterns = [
    path('terms/', TermsAndConditionsView.as_view(), name='terms_and_conditions')
]