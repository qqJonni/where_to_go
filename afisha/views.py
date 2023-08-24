from django.shortcuts import render
from places.models import PlaceName, Image
import json
from django.urls import reverse


def serialize_post(post):
    data = {
        "title": post.title,
        "imgs": [
            f'{pic.picturies.url}' for pic in post.pics.all().order_by('numb')
        ],
        "description_short": post.description_short,
        "description_long": post.description_long,
        "coordinates": {
            "lng": post.lon,
            "lat": post.lat
        }
    }
    with open(f"static/{post.slug}.json", "w") as outfile:
        json.dump(data, outfile)

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [post.point_lon, post.point_lat]
        },
        "properties": {
            "title": post.title.split("«")[1],
            "placeId": post.slug,
            "detailsUrl": f'static/{post.slug}.json'
        }
    }


def index(request):
    posts = PlaceName.objects.all()
    context = {
        'places_posts': {"type": "FeatureCollection",
                         "features": [
                             serialize_post(post) for post in posts
                         ]}
    }
    return render(request, 'index.html', context)

