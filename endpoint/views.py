from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from places.models import PlaceName


def serialize_post(post):
    post = {
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
    return post


def details_json(request, pk):
    post = get_object_or_404(PlaceName, pk=pk)
    post_data = serialize_post(post)
    output = JsonResponse(post_data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return HttpResponse(output, content_type="application/json")

