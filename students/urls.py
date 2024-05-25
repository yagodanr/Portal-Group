from django.contrib import admin
from django.urls import path
from .views import UserDetailView, ProjectDetailView, test, UserListView, GalleryPortfolioListView, GalleryProjectListView


urlpatterns = [
    path('portfolio/<int:pk>', UserDetailView.as_view(), name='detail-portfolio'),
    path('portfolio/<int:pk>/gallery', GalleryPortfolioListView.as_view(), name='detail-gallery-portfolio'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='detail-project'),
    path('project/<int:pk>/gallery', GalleryProjectListView.as_view(), name='detail-gallery-project'),
    path('list-of-users', UserListView.as_view(), name='users-list'),
    path('test', test, name='test'),
]
