from django.urls import path


from .views import Gradesheet

urlpatterns = [
    path('', Gradesheet.as_view(), name="gradesheet"),
] 