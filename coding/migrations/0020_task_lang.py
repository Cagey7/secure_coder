# Generated by Django 5.0.2 on 2024-04-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0019_alter_task_key_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='lang',
            field=models.CharField(default='python', max_length=63),
        ),
    ]
