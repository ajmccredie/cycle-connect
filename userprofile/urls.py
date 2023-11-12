from django.urls import path
from . import views
from userprofile.views import CustomSignupView

urlpatterns = [
    path('', views.index, name='index'),
    path('userprofile/signup_full_profile', views.signup_full_profile, name='signup_full_profile'),  
    path('account/signup', views.sign_up, name='sign_up'),
    path('account/logout', views.log_out, name='log_out'),
]