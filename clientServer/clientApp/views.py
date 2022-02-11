from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required


# Create your views here.

# @login_required(login_url='/login/')
def home(request):

    # Process in home view, maybe only showing html HOME template

    return HttpResponse("TEMP HOME")
    # return render(request, 'ATApp/home.html', {'products':products, 'logged':logged_val})

def login(request):

    # Process in login view:
    # OpenId Connect!!!
    # Fill with google API

    return HttpResponse("TEMP LOGIN")
    # return render(request, 'ATApp/contact.html', {'logged': logged_val})
