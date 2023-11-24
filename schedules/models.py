from django.db import models
from ships.models import Ship
from routes.models import Route

class Schedule(models.Model):
    name = models.CharField(verbose_name='Название расписания', max_length=100, unique=True)
    route = models.ForeignKey(Route,verbose_name="Название маршрута",on_delete=models.CASCADE)
    ship = models.ManyToManyField(Ship,verbose_name="Название судна")
    departure_date = models.DateField(verbose_name="День отбытия")
    arrival_date = models.DateField(verbose_name="День прибытия")

    def ships_names(self):
        return " %s" % (", ".join([Ship.name for Ship in self.ship.all()]))
    ships_names.short_description = 'Судна'  

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        
    