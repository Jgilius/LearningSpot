# Generated by Django 3.2.14 on 2022-09-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0051_auto_20220904_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_intention',
            name='lititle',
            field=models.CharField(blank=True, default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='learning_task',
            name='lttitle',
            field=models.CharField(blank=True, default=None, max_length=150),
        ),
    ]
