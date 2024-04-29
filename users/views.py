from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.db.models import Count
from coding.models import *
from .forms import *


def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    vulnerabilities = Vulnerability.objects.all().order_by("id")
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
    from django.shortcuts import get_object_or_404

    if not request.user.is_authenticated:
        return redirect("login")

    total_vulnerabilities = Task.objects.values('vulnerability') \
        .annotate(total=Count('vulnerability'))

    solved_vulnerabilities = SolvedTask.objects.filter(user=request.user) \
        .values('task__vulnerability') \
        .annotate(solved=Count('task__vulnerability')) \
        .order_by('task__vulnerability__name')

    vulnerabilities_count = {}
    for vulnerability_data in total_vulnerabilities:
        vulnerability = get_object_or_404(Vulnerability, pk=vulnerability_data['vulnerability'])
        vulnerabilities_count[vulnerability] = {
            'total': vulnerability_data['total'],
            'solved': 0
        }

    for solved_data in solved_vulnerabilities:
        vulnerability = get_object_or_404(Vulnerability, pk=solved_data['task__vulnerability'])
        vulnerabilities_count[vulnerability]['solved'] = solved_data['solved']

    return render(request, "users/profile.html", context={"vulnerabilities_count": vulnerabilities_count})


def logout_user(request):
    logout(request)
    return redirect("index")