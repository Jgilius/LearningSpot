# Generated by Django 3.2.14 on 2022-08-10 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lsbase', '0040_alter_learning_intention_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning_intention',
            name='unsure',
            field=models.ManyToManyField(blank=True, default=None, related_name='unsure', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Unsure_Select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Select', 'Select'), ('Unselect', 'Unselect')], default='Select', max_length=10)),
                ('learning_intention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lsbase.learning_intention')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
