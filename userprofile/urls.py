from django.urls import path
from . import views
from userprofile.views import CustomSignupView

urlpatterns = [
    path('', views.index, name='index'),
    path('userprofile/signup_full_profile', views.signup_full_profile, name='signup_full_profile'),  
    path('account/signup', views.signup, name='signup'),
    path('account/logout', views.logout, name='logout'),
]