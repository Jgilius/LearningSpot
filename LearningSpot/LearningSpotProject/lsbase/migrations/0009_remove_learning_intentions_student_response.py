# Generated by Django 3.2.14 on 2022-08-08 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0008_rename_reponse_learning_intentions_student_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning_intentions_student',
            name='response',
        ),
    ]