# Generated by Django 3.2.14 on 2022-08-08 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsbase', '0015_auto_20220808_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning_intention',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
