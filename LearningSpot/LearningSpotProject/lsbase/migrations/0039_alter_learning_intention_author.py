# Generated by Django 3.2.14 on 2022-08-10 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lsbase', '0038_alter_learning_intention_happy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_intention',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='auth.user'),
        ),
    ]
