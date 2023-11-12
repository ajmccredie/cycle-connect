from django.shortcuts import render

# Create your views here.
def userforum(request):
    return render(request, 'forum/userforum.html')

