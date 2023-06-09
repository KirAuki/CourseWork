# Generated by Django 4.2.2 on 2023-06-09 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название контейнера')),
                ('size', models.CharField(max_length=20, verbose_name='Размеры контейнера')),
                ('weight', models.FloatField(verbose_name='Вес контейнера')),
                ('date', models.DateField(auto_now_add=True, max_length=50, verbose_name='Дата принятия')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.schedule', verbose_name='Расписание')),
            ],
            options={
                'verbose_name': 'Контейнер',
                'verbose_name_plural': 'Контейнера',
            },
        ),
    ]
