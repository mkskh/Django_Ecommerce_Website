from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, UpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def update(request):

    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()

            login(request, current_user)
            messages.success(request, "User Has Been Updated")
            return redirect ("/")
        return render(request, "user/update.html", {"form": form})
    
    else:
        messages.success(request, "You Have To Be Logged In To Access")
        return redirect("user")


def registration(request):

    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'user/registration.html', {"form": form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user/login/')
        else:
            error = "You put wrong information. Please try again"
            return render(request, 'user/registration.html', {"form": form, "error": error})


def user_login(request):

    if request.method == "GET":
        return render(request, 'user/login.html', {})
    
    elif request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect('/')
        else:
            messages.error(request, ("Incorrect information were provided. Please try again"))
            return render(request, 'user/login.html', {})


def user_logout(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('/')


