from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
