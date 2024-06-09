from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Subject

# Create your views here.
class Gradesheet(ListView):
    model = Subject
    template_name = "gradesheet/gradesheet.html"
    context_object_name = "subjects"
    
class GradesheetSubject(DetailView):
    model = Subject
    template_name = "gradesheet/gradesheet_subject.html"
    