# Generated by Django 4.2.2 on 2023-06-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_alter_schedule_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название расписания'),
        ),
    ]
