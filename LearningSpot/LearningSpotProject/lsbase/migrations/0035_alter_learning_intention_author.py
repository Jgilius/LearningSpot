# Generated by Django 3.2.14 on 2022-08-10 04:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lsbase', '0034_alter_learning_intention_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_intention',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
