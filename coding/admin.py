from django.contrib import admin
from .models import *


@admin.register(Vulnerability)
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 10


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_per_page = 10


@admin.register(SolvedTask)
class TaskAdmin(admin.ModelAdmin):
    list_per_page = 10
    