# Generated by Django 4.2.2 on 2023-06-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название расписания'),
        ),
    ]
