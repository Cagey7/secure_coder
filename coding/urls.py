from django.urls import path
from . import views

urlpatterns = [
    path("tasks/<slug:vulnerability_slug>", views.vulnerability_list, name="tasks"),
    path("task/<slug:task_slug>", views.task_page, name="task"),
    path("check_task/<int:task_id>", views.check_task, name="check_task"),
    path("vulnerability/<slug:vulnerability_slug>", views.vulnerability_info, name="vulnerability"),
]
