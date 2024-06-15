from django.contrib import admin
from .models import Post, Branch

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'branch', 'author')
    list_display_links = ('id', 'name')

class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator')
    list_display_links = ('id', 'name', 'creator')


admin.site.register(Post, PostAdmin)
admin.site.register(Branch, BranchAdmin)
