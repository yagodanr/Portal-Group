from django.contrib import admin
from django.urls import path
from .views import BranchListView, BranchDetailView


urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branches/<int:pk>', BranchDetailView.as_view(), name='branch-detail'),
]
