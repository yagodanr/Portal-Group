from django.contrib import admin
from django.urls import path
from .views import BranchListView, BranchDetailView, BranchCreateView, PostCreateView


urlpatterns = [
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branch-create/', BranchCreateView.as_view(), name='branch-create'),
    path('branches/<int:pk>', BranchDetailView.as_view(), name='branch-detail'),
    path('post-create/<int:pk>', PostCreateView.as_view(), name='post-create'),
]
