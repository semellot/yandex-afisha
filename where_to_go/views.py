import json
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from places.models import Place, PlaceImage


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
                    'coordinates': [place.coordinate_lng, place.coordinate_lat]
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
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.coordinate_lng,
            'lat': place.coordinate_lat
        }
    }
    
    place_images = PlaceImage.objects.filter(place=place)
    for place_image in place_images:
        response_data['imgs'].append(place_image.image.url)
    
    return HttpResponse(json.dumps(response_data, ensure_ascii=False),
         content_type='application/json')
