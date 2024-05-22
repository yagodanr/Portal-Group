from django.contrib import admin
from django.urls import path
from .views import UserDetailView, ProjectDetailView, test, UserListView

urlpatterns = [
    path('portfolio/<int:pk>', UserDetailView.as_view(), name='detail-portfolio'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='detail-project'),
    path('list-of-users', UserListView.as_view(), name='users-list'),
    path('test', test, name='test'),
]
