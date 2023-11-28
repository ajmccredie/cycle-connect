"""cycleconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userprofile.views import CustomSignupView, index, sign_up, logout_view, account_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('sign_up/', include('userprofile.urls')),
    path('log_out/', include('userprofile.urls')),
    path('signup_full_profile/', include('userprofile.urls')),
    path('profile_view/', include('userprofile.urls')),
    path('userforum/', include('forum.urls')),
    path('bookable_services/', include('bookable_services.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login', account_login, name='account_login'),
    path('summernote/', include('django_summernote.urls')),
]
