import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Place, PlaceImage


def start_page(request):
    geo_json = {
        'type': 'FeatureCollection',
        'features': []
    }
    places = Place.objects.all()
    
    for place in places:
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
                    'detailsUrl': f'places/{place.id}'
                }
            }
        )
    
    return render(request, 'index.html', {'json': geo_json})


def detail_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
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
    
    for place_image in place.place_images:
        response_data['imgs'].append(place_image.image.url)
    
    return HttpResponse(json.dumps(response_data, ensure_ascii=False),
         content_type='application/json')
