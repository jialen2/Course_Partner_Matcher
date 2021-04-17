from django.forms import ModelForm
from django.forms import Form
from django import forms
from .models import Enrollment
from .models import Courses
from .models import LoginInfo
from .models import Students

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

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['NetId', 'FirstName', 'LastName', 'Preferred_Work_Time', 'SchoolYear', 'ContactInfo', 'OtherInfo']
