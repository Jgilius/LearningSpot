# Generated by Django 3.2.14 on 2022-08-08 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0005_alter_learning_intention_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning_intentions_student',
            name='learning_intention',
        ),
        migrations.RemoveField(
            model_name='learning_intentions_student',
            name='user',
        ),
        migrations.AddField(
            model_name='learning_intention_teacher',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
