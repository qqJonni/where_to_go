from django.db import models


class PlaceName(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description_short = models.TextField(null=True, blank=True)
    description_long = models.TextField(null=True, blank=True)
    coordinates = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=128, unique=True)
    imgs = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
