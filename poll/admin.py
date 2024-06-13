from django.contrib import admin

from .models import Poll, Option

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'last_edited')
    list_display_links = ('id', 'title')

class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'poll', )
    list_display_links = ('id', 'name')


admin.site.register(Poll, PollAdmin)
admin.site.register(Option, OptionAdmin)
