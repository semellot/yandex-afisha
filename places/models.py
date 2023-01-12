from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    
    description_short = models.TextField(verbose_name="Краткое описание")
    description_long = models.TextField(verbose_name="Полное описание")
    
    coordinate_lng = models.FloatField(verbose_name="Долгота")
    coordinate_lat = models.FloatField(verbose_name="Широта")
    
    def __str__(self):
        return self.title