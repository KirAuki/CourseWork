# Generated by Django 4.2.2 on 2023-06-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название судна')),
                ('capacity', models.IntegerField(verbose_name='Вместимость судна')),
                ('status', models.CharField(max_length=50, verbose_name='Статус судна')),
            ],
            options={
                'verbose_name': 'Судно',
                'verbose_name_plural': 'Судна',
            },
        ),
    ]
