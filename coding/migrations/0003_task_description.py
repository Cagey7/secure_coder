# Generated by Django 5.0.2 on 2024-03-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0002_task_vulnerability'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
