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
        action = request.POST.get("action")
        if action == "submit":
            user_answer = request.POST.get("user_answer")
            task = Task.objects.get(id=task_id)
            msg = check_python_code(user_answer)
            
            if task.lang == "python" and msg:
                messages.error(request, msg)
                return redirect(request.META.get("HTTP_REFERER", "index"))
                
            for word in task.key_words:
                if word not in user_answer:
                    msg = "The code still contains a vulnerability or incorrect input"
                    messages.error(request, msg)
                    return redirect(request.META.get("HTTP_REFERER", "index"))

            msg = "Correct answer 🙃"
            task = Task.objects.get(pk=task_id)
            user = request.user
            task.users.add(user)
            messages.success(request, msg)
            return redirect(request.META.get("HTTP_REFERER", "index"))
        elif action == "ask_gpt":
            user_answer = request.POST.get("user_answer")
            
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": f"Дай подсказу об уязвимостях в коде"},
                    {"role": "user", "content": f"{user_answer}"}
                ]
            )
            gpt_answer = completion.choices[0].message.content
            messages.info(request, gpt_answer)
            return redirect(request.META.get("HTTP_REFERER", "index"))


def vulnerability_info(request, vulnerability_slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    vulnerability = Vulnerability.objects.get(slug=vulnerability_slug)
    context = {
        "vulnerability": vulnerability,
    }
    return render(request, "coding/vulnerability_info.html", context=context)
