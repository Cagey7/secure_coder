# Generated by Django 5.0.2 on 2024-04-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0010_gptquestion_compare_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gptquestion',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='gpt_questions',
            field=models.ManyToManyField(to='coding.gptquestion'),
        ),
    ]
