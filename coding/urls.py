from django.urls import path
from . import views

urlpatterns = [
    path("vulnerability", views.home_vulnerability, name="home_vulnerability"),
    path("vulnerability/<slug:vulnerability_slug>", views.vulnerability_list, name="vulnerability"),
    path("task/<slug:task_slug>", views.task_page, name="task"),
    path("check_task/<int:task_id>", views.check_task, name="check_task"),
]
