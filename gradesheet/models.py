from django.db import models
from django.conf import settings

# Create your models here.
class Grade(models.Model):
    grade = models.IntegerField()
    subject = models.CharField(max_length=255) #Тимчасово так, а потім подивимось чи буде воно треба і як писатимемо
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="grades")
    
    

