from django.db import models
from ships.models import Ship
from routes.models import Route

class Schedule(models.Model):
    name = models.CharField(verbose_name="Название расписания",max_length=100,unique=True)
    ship = models.ForeignKey(Ship,verbose_name="Название судна",on_delete=models.CASCADE)
    route = models.ForeignKey(Route,verbose_name="Название маршрута",on_delete=models.CASCADE)
    departure_date = models.DateField(verbose_name="День отбытия")
    arrival_date = models.DateField(verbose_name="День прибытия")
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
