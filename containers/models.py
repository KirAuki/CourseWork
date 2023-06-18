from django.db import models
from schedules.models import Schedule

class Container(models.Model):
    name = models.CharField(verbose_name='Название контейнера',max_length=100, unique=True)
    schedule = models.ForeignKey(Schedule,verbose_name="Расписание",on_delete=models.CASCADE)
    size = models.CharField(verbose_name='Размеры контейнера',max_length=20)
    weight = models.FloatField(verbose_name='Вес контейнера',)
    date = models.DateField(verbose_name='Дата принятия', auto_now_add=True, max_length=50)
    done = models.BooleanField(verbose_name='Доставлено',default= False)
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Контейнер"
        verbose_name_plural = "Контейнера" 