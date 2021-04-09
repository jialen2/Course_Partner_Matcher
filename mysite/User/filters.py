import django_filters
from .models import *

class LoginInfoFilter(django_filters.FilterSet):
    class Meta:
        model = LoginInfo
        fields = ['AccountName']

class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Students
        fields = ['NetId']

class CoursesFilter(django_filters.FilterSet):
    class Meta:
        model = Courses
        fields = ['CRN']