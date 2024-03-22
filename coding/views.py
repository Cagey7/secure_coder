from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Task, Vulnerability


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
    context = {
        "vulnerabilities": vulnerabilities,
        "tasks": tasks,
    }
    return render(request, "coding/vulnerability.html", context=context)


def task_page(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    context = {
        "task": task
    }
    return render(request, "coding/task.html", context=context)
