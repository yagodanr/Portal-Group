from django.contrib import admin


from .models import Subject, Grade

# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', )
    list_display_links = ('id', 'name', )
    
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade', 'subject', 'student', 'project', 'date', )
    

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Grade, GradeAdmin)
    