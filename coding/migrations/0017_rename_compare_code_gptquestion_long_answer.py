# Generated by Django 5.0.2 on 2024-04-22 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0016_alter_task_gpt_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gptquestion',
            old_name='compare_code',
            new_name='long_answer',
        ),
    ]