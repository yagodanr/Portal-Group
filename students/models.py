from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    authors = models.ManyToManyField(User, related_name='projects')
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=127)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='portfolio')
    description = models.TextField()
