from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request, 'profile.html')
       
    else:    
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form } )

def profile(request):
    return render(request, 'accounts/profile.html')