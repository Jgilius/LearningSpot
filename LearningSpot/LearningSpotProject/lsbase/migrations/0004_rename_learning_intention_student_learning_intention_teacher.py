# Generated by Django 3.2.14 on 2022-08-08 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0003_learning_intention_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='learning_intention_student',
            new_name='learning_intention_teacher',
        ),
    ]