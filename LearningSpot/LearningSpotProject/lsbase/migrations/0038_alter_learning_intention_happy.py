# Generated by Django 3.2.14 on 2022-08-10 05:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lsbase', '0037_auto_20220810_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_intention',
            name='happy',
            field=models.ManyToManyField(blank=True, default=None, related_name='happy', to=settings.AUTH_USER_MODEL),
        ),
    ]
