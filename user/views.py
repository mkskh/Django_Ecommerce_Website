from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, UpdateForm, UpdateUserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from . import models


@login_required
def update(request):
    current_user = request.user
    profile = models.UserProfile.objects.filter(user=current_user).first()

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=current_user)
        form2 = UpdateUserInfoForm(request.POST)

        if form.is_valid() and form2.is_valid():
            form.save()
            
            phone = request.POST["phone"]
            address = request.POST["address"]
            additional_address = request.POST["additional_address"]
            city = request.POST["city"]
            region = request.POST["region"]
            zip_code = request.POST["zip_code"]
            country = request.POST["country"]
            
            profile.phone = phone
            profile.address = address
            profile.additional_address = additional_address
            profile.city = city
            profile.region = region
            profile.zip_code = zip_code
            profile.country = country

            profile.save()

            messages.success(request, "User information has been updated.")
            return redirect("/")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UpdateForm(instance=current_user)
        form2 = UpdateUserInfoForm(instance=profile)

    return render(request, "user/update.html", {"form": form, "form2": form2})


def registration(request):

    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'user/registration.html', {"form": form})
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/user/login/')
        else:
            error = "You put wrong information. Please try again"
            return render(request, '/user/registration.html', {"form": form, "error": error})


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


