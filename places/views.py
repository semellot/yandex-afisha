from django.db.models import Prefetch
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Place, PlaceImage


def start_page(request):
    geo_json = {
        'type': 'FeatureCollection',
        'features': []
    }
    
    for place in Place.objects.all():
        geo_json['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('places', args=(place.id,))
                }
            }
        )
    
    return render(request, 'index.html', {'json': geo_json})


def detail_place(request, place_id):
    place = Place.objects.prefetch_related(Prefetch('place_images')).get(pk=place_id)
    response_data = {
        'title': place.title,
        'imgs': [],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    
    for place_image in place.place_images.all():
        response_data['imgs'].append(place_image.image.url)
    
    return JsonResponse(response_data)
