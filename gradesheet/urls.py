from django.urls import path


from .views import Gradesheet, GradesheetSubject

urlpatterns = [
    path('', Gradesheet.as_view(), name="gradesheet"),
    path('<int:pk>/', GradesheetSubject.as_view(), name="gradesheet-subject"),
] 