from django.db import models
from django.conf import settings


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)

class Project(models.Model):
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='projects')
    gallery = models.ManyToManyField(GalleryImage, blank=True)
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='portfolio')
    gallery = models.ManyToManyField(GalleryImage, blank=True)
    description = models.TextField()
