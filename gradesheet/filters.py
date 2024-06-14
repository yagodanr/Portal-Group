import django_filters
from .models import Grade


class GradeFilter(django_filters.FilterSet):
    grade = django_filters.RangeFilter()
    
    
    class Meta:
        model = Grade
        fields = {
            'subject__name': ["icontains"],
            'student__username': ["icontains"],
            'project__name': ["icontains"],
            'date': ["iexact"]
        }