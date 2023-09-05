from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Image = models.ImageField(upload_to='user_images', null=True, blank=True)

