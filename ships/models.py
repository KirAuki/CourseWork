from django.db import models

class Ship(models.Model):
    name = models.CharField(verbose_name="Название судна" ,max_length=100, unique=True)
    capacity = models.IntegerField(verbose_name="Вместимость судна")
    status = models.CharField(verbose_name="Статус судна",max_length=50)

    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Судно"
        verbose_name_plural = "Судна"