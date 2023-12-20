from django.urls import path
from . import views
from userprofile.views import CustomSignupView, LogoutView, AccountLoginView, ProfileView, SignUpView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/login/', AccountLoginView.as_view(), name='account_login'),
    path('signup_full_profile/', views.signup_full_profile, name='signup_full_profile'),  
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('log_out/', LogoutView.as_view(), name='log_out'),
    path('profile_view/', ProfileView.as_view(), name='profile_view'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('profile/', ProfileView.as_view(), name='profile'),
]