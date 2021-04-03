from django.forms import ModelForm
from .models import Enrollment
from .models import Courses

class Form(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['NetId', 'CRN']

class Courses(ModelForm):
    class Meta:
        model = Courses
        fields = ['CRN', 'CourseTitle', 'CourseNumber', 'Department', 'Section', 'ScheduleType', 'Instructor', 'MeetingTime']