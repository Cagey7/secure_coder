# Generated by Django 5.0.2 on 2024-04-17 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0013_remove_gptquestion_negative_gptquestion_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gptquestion',
            options={'ordering': ['order']},
        ),
    ]
