from django.views.generic import DetailView, ListView
from .models import Project, Portfolio

from auth_sys.models import MyUser
# Create your views here.


class PortfolioListView(ListView):
    model = Portfolio
    template_name = "students/portfolio-list.html"
    context_object_name = 'portfolios'

class ProjectListView(ListView):
    model = Project
    template_name = "students/project-list.html"
    context_object_name = 'projects'


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'students/portfolio.html'
    context_object_name = 'portfolio'
    

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'students/project.html'
    context_object_name = 'project'


class GalleryPortfolioListView(DetailView):
    model = Portfolio
    template_name = 'students/portfolio-gallery.html'
    context_object_name = 'portfolio'


class GalleryProjectListView(DetailView):
    model = Project
    template_name = 'students/project-gallery.html'
    context_object_name = 'project'


def test(request):
    a = MyUser.objects.get(id=1)
    b = a.portfolio.first().gallery.last().image.url
    print(b)
