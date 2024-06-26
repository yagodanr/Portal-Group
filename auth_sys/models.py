from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe


# Create your models here.
class MyUser(AbstractUser):
    photo = models.ImageField(upload_to="task_manager/comment/%Y/%m/%d/", blank=True, null=True)
    def admin_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width=100>')
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self) -> str:
        return self.username
    