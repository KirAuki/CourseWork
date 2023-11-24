# Generated by Django 4.2.2 on 2023-06-29 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
        ('containers', '0005_alter_container_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.schedule', verbose_name='Расписание'),
        ),
    ]