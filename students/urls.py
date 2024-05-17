from django.contrib import admin
from django.urls import path
from .views import UserDetailView, ProjectDetailView, test

urlpatterns = [
    path('portfolio/<int:pk>', UserDetailView.as_view(), name='portfolio'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project'),
    path('test', test, name='test'),
]
