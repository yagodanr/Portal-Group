from django.urls import path

from .views import PollListView, PollDetailView


urlpatterns = [
    path("", PollListView.as_view(), name="list-poll"),
    path("<int:pk>/", PollDetailView.as_view(), name="detail-poll")
] 