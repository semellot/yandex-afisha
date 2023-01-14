from django.shortcuts import render

from places.models import Place


def start_page(request):
    json = {
        'type': 'FeatureCollection',
        'features': []
    }
    places = Place.objects.all()
    
    for place in places:
        json['features'].append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.coordinate_lng, place.coordinate_lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': '/static/places/moscow_legends.json'
                }
            }
        )
    
    return render(request, 'index.html', {'json': json})
