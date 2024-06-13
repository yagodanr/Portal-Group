from django.db import models
from django.conf import settings



# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Poll"        
        verbose_name_plural = "Polls"        
        

class Option(models.Model):
    name = models.CharField(max_length=255)
    voted = models.ManyToManyField(settings.AUTH_USER_MODEL)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["poll"]
        verbose_name = "Option"        
        verbose_name_plural = "Options"        

    
    