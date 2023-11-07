from django.urls import path
from . import views
from userprofile.views import CustomSignupView

urlpatterns = [
    path('', views.index, name='index'),  
    path('signup/', CustomSignupView.as_view()),
]