from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    hint = models.CharField(max_length=511)
    func_input = ArrayField(models.CharField())
    func_output = ArrayField(models.CharField())
    key_words = ArrayField(models.CharField())
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.PROTECT)

    def __str__(self):
        return f"Vulnerability: {self.name}"
