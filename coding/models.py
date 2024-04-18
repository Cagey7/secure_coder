from django.db import models
from django.contrib.auth import get_user_model


class Vulnerability(models.Model):
    name = models.CharField(max_length=127, verbose_name="vulnerability name")
    slug = models.CharField(max_length=127, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"Vulnerability: {self.name}"


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name="task name")
    description = models.TextField()
    slug = models.CharField(max_length=127, unique=True)
    code_task = models.TextField()
    solution = models.TextField()
    hint = models.TextField()
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.PROTECT)
    gpt_questions = models.ManyToManyField("GptQuestion")
    users = models.ManyToManyField(get_user_model(), through="SolvedTask")

    def __str__(self):
        return f"Vulnerability: {self.name}"


class GptQuestion(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=127)
    order = models.IntegerField(default=100)
    compare_code = models.BooleanField(default=False)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.question}"


class SolvedTask(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
