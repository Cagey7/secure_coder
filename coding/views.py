from django.shortcuts import render, redirect
from .models import Task, Vulnerability, SolvedTask
from django.contrib import messages
from .utils import *


def vulnerability_list(request, vulnerability_slug):
    if not request.user.is_authenticated:
        return redirect("login")

    vulnerability = Vulnerability.objects.get(slug=vulnerability_slug)
    tasks = Task.objects.filter(vulnerability_id=vulnerability.id)
    vulnerabilities = Vulnerability.objects.all().order_by("id")
    user = request.user

    context = {
        "vulnerabilities": vulnerabilities,
        "tasks": tasks,
        "user": user,
        "selected_vulnerability": vulnerability,
    }
    return render(request, "coding/vulnerability_tasks.html", context=context)


def task_page(request, task_slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    task = Task.objects.get(slug=task_slug)
    user = request.user
    is_solved = SolvedTask.objects.filter(task=task, user=user).exists()
    context = {
        "task": task,
        "is_solved": is_solved,
    }
    return render(request, "coding/task.html", context=context)


def check_task(request, task_id):
    if request.method == "POST":
        user_answer = request.POST.get("user_answer")
        task = Task.objects.get(id=task_id)

        for question in task.gpt_questions.all():
            if question.order == 2:
                continue
            print(question.question)
            if question.compare_code:
                if ask_chatgpt(question.question, f"Первый код:{task.code_task}, \n второй код:{user_answer}"):
                    messages.error(request, question.answer)
                    return redirect(request.META.get("HTTP_REFERER", "index"))
            else:
                if ask_chatgpt(question.question, user_answer):
                    messages.error(request, question.answer)
                    return redirect(request.META.get("HTTP_REFERER", "index"))
        msg = "Задание выполнено верно🙃"
        # task = Task.objects.get(pk=task_id)
        # user = request.user
        # task.users.add(user)
        messages.error(request, msg)
        return redirect(request.META.get("HTTP_REFERER", "index"))


def vulnerability_info(request, vulnerability_slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    vulnerability = Vulnerability.objects.get(slug=vulnerability_slug)
    context = {
        "vulnerability": vulnerability,
    }
    return render(request, "coding/vulnerability_info.html", context=context)
