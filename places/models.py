from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from tinymce import models as tinymce_models

from afisha import settings


class PlaceName(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True, null=True)
    long_description = tinymce_models.HTMLField('Полное описание', blank=True, null=True)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    point_lon = models.FloatField(verbose_name="Долгота точки", blank=True, null=True)
    point_lat = models.FloatField(verbose_name="Широта точки", blank=True, null=True)
    slug = models.SlugField('Название в виде url', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Image(models.Model):
    numb = models.IntegerField(verbose_name="Порядковый номер:", db_index=True)
    title = models.ForeignKey(PlaceName, on_delete=models.CASCADE, verbose_name="Заголовок", related_name='pics')
    picturies = models.ImageField(verbose_name="Картинка", upload_to='img', blank=True)

    def __str__(self):
        return f'{self.numb} {self.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['numb']

    @property
    def photo_preview(self):
        if self.picturies:
            return format_html('<img src="{}" height="200" />'.format(self.picturies.url))
        return ""

    @property
    def get_absolute_image_url(self):
        return "{0}{1}".format(settings.MEDIA_URL, self.picturies.url)
