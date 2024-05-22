from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Project

# Create your views here.


class UserDetailView(DetailView):
    model = User
    template_name = 'users/portfolio.html'
    context_object_name = 'user'


class UserListView(ListView):
    model = User
    template_name = 'users/users-list.html'
    context_object_name = 'users'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'users/project.html'
    context_object_name = 'project'

def test(request):
    a = Project.objects.get(id=1)
    for author in a.authors.all():
        print(author.projects.all())
