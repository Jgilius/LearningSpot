# Generated by Django 3.2.14 on 2022-08-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0019_learning_intention_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learning_intention',
            name='text',
        ),
        migrations.AlterField(
            model_name='learning_intention',
            name='li',
            field=models.CharField(max_length=20),
        ),
    ]