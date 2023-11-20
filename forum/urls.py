from django.urls import path
from .views import UserPost

urlpatterns = [
    path('userforum/', UserPost.as_view(), name="userforum"),
]