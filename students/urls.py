from django.contrib import admin
from django.urls import path
from .views import PortfolioListView, ProjectListView, PortfolioDetailView, ProjectDetailView, test, GalleryPortfolioListView, GalleryProjectListView


urlpatterns = [
    path('portfolio/', PortfolioListView.as_view(), name='list-portfolio'),
    path('portfolio/<int:pk>', PortfolioDetailView.as_view(), name='detail-portfolio'),
    path('portfolio/<int:pk>/gallery', GalleryPortfolioListView.as_view(), name='detail-gallery-portfolio'),
    path('project/', ProjectListView.as_view(), name='list-project'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='detail-project'),
    path('project/<int:pk>/gallery', GalleryProjectListView.as_view(), name='detail-gallery-project'),
    path('test', test, name='test'),
]
