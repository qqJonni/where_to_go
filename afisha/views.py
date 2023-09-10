from django.shortcuts import render
from django.urls import reverse
import json

from places.models import PlaceName, Image


def serialize_post(post):
    redirect_url = reverse("details-json", args=[post.pk])

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [post.longitude, post.latitude]
        },
        "properties": {
            "title": post.title,
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

