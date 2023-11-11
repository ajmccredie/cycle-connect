from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.userforum, name="userforum")
]