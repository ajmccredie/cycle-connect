from django.urls import path
from . import views

urlpatterns = [
    path('userforum/', views.userforum, name="userforum")
]