from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from .models import Project, GalleryImage

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


class GalleryPortfolioListView(DetailView):
    model = User
    template_name = 'users/portfolio-gallery.html'
    context_object_name = 'user'


class GalleryProjectListView(DetailView):
    model = Project
    template_name = 'users/project-gallery.html'
    context_object_name = 'project'


def test(request):
    a = User.objects.get(id=1)
    b = a.portfolio.first().gallery.last().image.url
    print(b)
