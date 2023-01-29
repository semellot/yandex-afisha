from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок',
        unique=True
    )
    
    order = models.PositiveIntegerField(
        verbose_name='Сортировка',
        default=0,
        blank=True,
        null=False
    )
    
    short_description = models.TextField(
        verbose_name='Краткое описание',
        blank=True
    )
    long_description = HTMLField(
        verbose_name='Полное описание',
        blank=True
    )
    
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order',]


class PlaceImage(models.Model):
    image = models.ImageField(
        verbose_name='Изображение',
        blank=False
    )
    
    order = models.PositiveIntegerField(
        verbose_name='Сортировка',
        default=0,
        blank=True,
        null=False
    )
    
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='images'
    )
    
    def __str__(self):
        return self.place.title
    
    class Meta:
        ordering = ['order',]
