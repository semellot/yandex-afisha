import os
from urllib.parse import urlparse

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage

import requests
from PIL import Image
from io import BytesIO


class Command(BaseCommand):
    help = 'Создание точек с локациями'
    
    def add_arguments(self, parser):
        parser.add_argument('json_url')
    
    def handle(self, *args, **options):
        response = requests.get(options['json_url'])
        response.raise_for_status()
        
        json_place = response.json()
        
        place, created = Place.objects.get_or_create(
            title=json_place['title'],
            short_description=json_place['description_short'],
            long_description=json_place['description_long'],
            longitude=json_place['coordinates']['lng'],
            latitude=json_place['coordinates']['lat'],
        )
        
        for image_url in json_place['imgs']:            
            response_image = requests.get(image_url)
            response_image.raise_for_status()
            
            place_image = PlaceImage.objects.create(place=place)
            
            image = BytesIO(response_image.content)
            
            image_url_parsed = urlparse(image_url)
            filename = os.path.basename(image_url_parsed.path)
            
            place_image.image.save(
                filename,
                ContentFile(image.getvalue()),
                save=True
            )
        
        print(f'Добавлена локация с названием: {place.title}')
