from django.shortcuts import render, redirect
from .models import Task, Vulnerability, SolvedTask
from django.contrib.auth import get_user_model


def home_vulnerability(request):
    vulnerabilities = Vulnerability.objects.all()
    context = {
        "vulnerabilities": vulnerabilities,
    }
    return render(request, "coding/home_vulnerability.html", context=context)


def vulnerability_list(request, vulnerability_slug):
    vulnerability_id = Vulnerability.objects.get(slug=vulnerability_slug).id
    tasks = Task.objects.filter(vulnerability_id=vulnerability_id)
    vulnerabilities = Vulnerability.objects.all()
    user = request.user

    context = {
        "vulnerabilities": vulnerabilities,
        "tasks": tasks,
        "user": user,
    }
    return render(request, "coding/vulnerability.html", context=context)


def task_page(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    user = request.user
    is_solved = SolvedTask.objects.filter(task=task, user=user).exists()
    context = {
        "task": task,
        "is_solved": is_solved,
    }
    return render(request, "coding/task.html", context=context)


def check_task(request, task_id):
    if request.method == 'POST':
        user_answer = request.POST.get('user_answer') 
        task = Task.objects.get(pk=task_id)
        user = request.user
        task.users.add(user)

        return redirect(request.META.get('HTTP_REFERER', 'index'))
