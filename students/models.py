from django.db import models
from django.contrib.auth.models import User


class GalleryImage(models.Model):
    image = models.ImageField(blank=True, null=True)

class Project(models.Model):
    authors = models.ManyToManyField(User, related_name='projects')
    gallery = models.ManyToManyField(GalleryImage, blank=True, null=True)
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='portfolio')
    gallery = models.ManyToManyField(GalleryImage, blank=True, null=True)
    description = models.TextField()
