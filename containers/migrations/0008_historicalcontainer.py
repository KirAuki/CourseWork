# Generated by Django 4.1.5 on 2023-11-24 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_alter_schedule_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('containers', '0007_alter_container_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalContainer',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Название контейнера')),
                ('size', models.CharField(max_length=20, verbose_name='Размеры контейнера')),
                ('weight', models.FloatField(verbose_name='Вес контейнера')),
                ('date', models.DateField(blank=True, editable=False, max_length=50, verbose_name='Дата принятия')),
                ('done', models.BooleanField(default=False, verbose_name='Доставлено')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='schedules.schedule', verbose_name='Расписание')),
            ],
            options={
                'verbose_name': 'historical Контейнер',
                'verbose_name_plural': 'historical Контейнера',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
