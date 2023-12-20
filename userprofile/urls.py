from django.urls import path
from . import views
from userprofile.views import CustomSignupView, LogoutView, AccountLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', AccountLoginView.as_view(), name='account_login'),
    path('signup_full_profile/', views.signup_full_profile, name='signup_full_profile'),  
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', LogoutView.as_view(), name='log_out'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('profile/', views.profile_view, name='profile'),
]