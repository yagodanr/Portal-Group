from django.shortcuts import render
from django.views.generic import ListView

from .models import Subject

# Create your views here.
class Gradesheet(ListView):
    model = Subject
    template_name = "gradesheet/gradesheet.html"
    context_object_name = "subjects"
    