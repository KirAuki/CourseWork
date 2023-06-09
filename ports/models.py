from django.db import models


class DeparturePort(models.Model):
    name = models.CharField(verbose_name='Название порта отправки', max_length=100, unique=True)
    country = models.CharField(verbose_name='Страна порта отправки', max_length=100)
    city = models.CharField(verbose_name='Город порта отправки', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Порт отправки"
        verbose_name_plural = "Порты отправки"


class ArrivalPort(models.Model):
    name = models.CharField(verbose_name='Название порта назначения', max_length=100, unique=True)
    country = models.CharField(verbose_name='Страна порта назначения', max_length=100)
    city = models.CharField(verbose_name='Город порта назначения', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Порт назначения"
        verbose_name_plural = "Порты назначения"