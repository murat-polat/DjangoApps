from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
### Messages ####
# # Change the messages level to ensure the debug message is added.
# messages.set_level(request, messages.DEBUG)
# messages.debug(request, "Test message...")

# # In another request, record only messages with a level of WARNING and higher
# messages.set_level(request, messages.WARNING)
# messages.success(request, "Your profile was updated.")  # ignored
# messages.warning(request, "Your account is about to expire.")  # recorded




def home_(request):
    return render(request, 'home.html')

def login_(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request, 'profile.html')
       
    else:    
        return render(request, 'login.html')

def register_(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Thanks for registrations. Now you can login the page.")
            # return render(request, 'login.html')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form } )

def profile_(request):
    return render(request, 'accounts/profile.html')

def logout_(request):
    logout(request)
    messages.success(request, "You are logout.")
    return render(request, 'home.html')


def dashboard_(request):
    return render(request, 'dashboard.html')