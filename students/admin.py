from django.contrib import admin
from .models import Portfolio, Project, GalleryImage

# Register your models here.

admin.site.register(Project)
admin.site.register(Portfolio)
admin.site.register(GalleryImage)
