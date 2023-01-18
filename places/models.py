from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    
    coordinate_lng = models.FloatField(verbose_name='Долгота')
    coordinate_lat = models.FloatField(verbose_name='Широта')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title',]


class PlaceImage(models.Model):
    image = models.ImageField(verbose_name='Изображение')
    
    order = models.PositiveIntegerField(
        verbose_name='Сортировка',
        default=0,
        blank=False,
        null=False
    )
    
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место'
    )
    
    def __str__(self):
        return self.place.title
    
    class Meta:
        ordering = ['order',]
