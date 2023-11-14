from django.shortcuts import render, get_object_or_404
from django.views import generic, View

# Create your views here.
def userforum(request):
    return render(request, 'userforum.html')



