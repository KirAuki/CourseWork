# Generated by Django 4.2.2 on 2023-06-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Погружено'),
        ),
    ]