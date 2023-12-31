# Generated by Django 4.2.5 on 2023-09-05 15:57

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PlaceName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                (
                    "short_description",
                    models.TextField(blank=True, verbose_name="Короткое описание"),
                ),
                (
                    "long_description",
                    tinymce.models.HTMLField(
                        blank=True, verbose_name="Полное описание"
                    ),
                ),
                (
                    "longitude",
                    models.FloatField(blank=True, verbose_name="Долгота точки"),
                ),
                (
                    "latitude",
                    models.FloatField(blank=True, verbose_name="Широта точки"),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "numb",
                    models.IntegerField(
                        db_index=1, null=True, verbose_name="Порядковый номер:"
                    ),
                ),
                (
                    "picture",
                    models.ImageField(upload_to="img", verbose_name="Картинка"),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pics",
                        to="places.placename",
                        verbose_name="Заголовок",
                    ),
                ),
            ],
            options={
                "verbose_name": "Картинка",
                "verbose_name_plural": "Картинки",
                "ordering": ["numb"],
            },
        ),
    ]
