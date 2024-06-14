from django.db import models
from django.conf import settings

# Create your models here.

class Branch(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='branch')
    name = models.CharField(max_length=255)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='post')
    branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING, related_name='post')
    name = models.CharField(max_length=255)
    text = models.TextField()
    media = models.FileField(upload_to='post-media/', blank=True, null=True)
