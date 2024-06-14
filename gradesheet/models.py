from django.db import models
from django.conf import settings

from students.models import Project


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="subjects")
    
    
    def __str__(self) -> str:
        return f"{self.name}: {self.teacher}"

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
    
    
class Grade(models.Model):
    grade = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="grades")
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="grades")
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="grades")
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.subject}:\n{self.date} "

    class Meta:
        ordering = ["-date", "student"]
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
        
    