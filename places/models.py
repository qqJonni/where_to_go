from django.db import models


class PlaceName(models.Model):
    title = models.CharField(max_length=128, unique=True)
    imgs = models.URLField(max_length=256)
    description_short = models.TextField(null=True, blank=True)
    description_long = models.TextField(null=True, blank=True)
    coordinates = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
