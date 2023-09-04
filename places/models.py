from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from tinymce import models as tinymce_models

from afisha import settings


class PlaceName(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = tinymce_models.HTMLField('Полное описание', blank=True)
    longitude = models.FloatField(verbose_name="Долгота точки", blank=True, null=False)
    latitude = models.FloatField(verbose_name="Широта точки", blank=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Image(models.Model):
    numb = models.IntegerField(verbose_name="Порядковый номер:", db_index=1, null=True)
    place = models.ForeignKey(PlaceName, on_delete=models.CASCADE, verbose_name="Заголовок", related_name='pics')
    picture = models.ImageField(verbose_name="Картинка", upload_to='img', blank=False)

    def __str__(self):
        return f'{self.numb} {self.place}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
        ordering = ['numb']

    @property
    def get_preview(self):
        if self.picture:
            return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;"/>', self.picture.url)
        return ""
