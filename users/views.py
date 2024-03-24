from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from coding.models import *
from .forms import *


def index(request):
    vulnerabilities = Vulnerability.objects.all()
    context = {
        "vulnerabilities": vulnerabilities
    }
    return render(request, "users/index.html", context=context)


def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = LoginUserForm()
    context = {
        "form": form,
        "title": "Логин"
    }
    return render(request, "users/login.html", context=context)


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    
    context = {
        "form": form,
        "title": "Регистрация"
    }
    return render(request, "users/register.html", context=context)


def profile(request):
    return render(request, "users/profile.html")


def logout_user(request):
    logout(request)
    return redirect("index")