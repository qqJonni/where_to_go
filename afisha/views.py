from django.shortcuts import render
from places.models import PlaceName, Image
import json
from django.urls import reverse


def serialize_post(post):
    redirect_url = reverse("details-json", args=[post.pk])

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [post.point_lon, post.point_lat]
        },
        "properties": {
            "title": post.title,
            "placeId": post.slug,
            "detailsUrl": redirect_url
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

