from django.urls import path
from . import views
from userprofile.views import CustomSignupView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.account_login, name='account_login'),
    path('signup_full_profile/', views.signup_full_profile, name='signup_full_profile'),  
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', views.logout_view, name='log_out'),
    path('profile_view/', views.profile_view, name='profile_view'),
]