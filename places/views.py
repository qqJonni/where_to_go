from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from places.models import PlaceName


def serialize_post(post):
    post = {
        "title": post.title,
        "imgs": [
            f'{pic.picture.url}' for pic in post.pics.all().order_by('numb')
        ],
        "short_description": post.short_description,
        "long_description": post.long_description,
        "coordinates": {
            "longitude": post.longitude,
            "latitude": post.latitude
        }
    }
    return post


def details_json(request, pk):
    post = get_object_or_404(PlaceName, pk=pk)
    post_data = serialize_post(post)
    return HttpResponse(JsonResponse(post_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4}), content_type="application/json")

