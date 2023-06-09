from django.db import models
from schedules.models import Schedule

class Raport(models.Model):
    name = models.CharField(verbose_name='Название Отчёта',max_length=100, unique=True)
    schedule = models.ForeignKey(Schedule,verbose_name='Название расписания',on_delete=models.CASCADE)
    delivery_status = models.CharField(verbose_name='Статус', max_length=50)

    def __str__(self):
        return self.name


    class Meta:
            verbose_name = "Отчёт"
            verbose_name_plural = "Отчёты"
    