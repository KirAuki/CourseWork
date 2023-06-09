from django.db import models
from ports.models import DeparturePort,ArrivalPort
class Route(models.Model):
    name = models.CharField(verbose_name='Название маршрута', max_length=100, unique=True)
    departure = models.ForeignKey(DeparturePort,verbose_name='Порт отправки',on_delete=models.CASCADE)
    arrival = models.ForeignKey(ArrivalPort,verbose_name='Порт назначения',on_delete=models.CASCADE)
    distance = models.FloatField(verbose_name='Дистанция')
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"

        