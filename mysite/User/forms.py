from django.forms import ModelForm
from .models import Enrollment
from .models import Courses
from .models import LoginInfo

class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['NetId', 'CRN']

class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['CRN', 'CourseTitle', 'CourseNumber', 'Department', 'Section', 'ScheduleType', 'Instructor', 'MeetingTime']

class LoginInfoForm(ModelForm):
    class Meta:
        model = LoginInfo
        fields = ['AccountName', 'Password']