# Generated by Django 3.2.14 on 2022-09-04 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0046_alter_learning_intention_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learning_intention',
            old_name='title',
            new_name='lititle',
        ),
        migrations.RenameField(
            model_name='learning_task',
            old_name='title',
            new_name='lttitle',
        ),
    ]