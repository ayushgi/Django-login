import email
from click import password_option
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
# Create your views here.
def index(request):
    # For checking anonymous user 
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def login(request):
    # For authentication of username and password 
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user =authenticate(email=email,password=password)
        if user is not None:
            return redirect('/')
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutuser(request):
    logout()
    return redirect("login.html")    
    
