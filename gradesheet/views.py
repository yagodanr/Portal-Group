from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Subject, Grade
from .filters import GradeFilter

# Create your views here.
class Gradesheet(ListView):
    model = Grade
    template_name = "gradesheet/gradesheet1.html"
    context_object_name = "grades"
    ordering = ["-date"]
    paginate_by = 2
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        self.filterset = GradeFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form

        return context
    

class GradesheetOld(ListView):
    model = Subject
    template_name = "gradesheet/gradesheet.html"
    context_object_name = "subjects"
    
    
    
class GradesheetSubject(DetailView):
    model = Subject
    template_name = "gradesheet/gradesheet-subject.html"
    