from django.shortcuts import render

# import forms & models
from .forms import SignUpForm


# Create your views here.


def home(request):
    return render(request, 
		  'home.html' )
	

def base(request):
    return render(request,
                  'base.html',)


def faq(request):
    return render(request,
                  'faq.html',)
def signup(request):
    if request.method == "GET":
        return render(request,
                      'signup.html',
                      {'form' : SignUpForm})
    #elif request.method == "POST":
     #   return render(re
