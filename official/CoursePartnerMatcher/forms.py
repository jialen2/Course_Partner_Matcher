from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = ['NetId', 'Department']

class EnrollmentForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['NetId', 'CRN']

class CoursesForm(ModelForm):
    class Meta:
        model = Courses
        fields = ['CRN', 'CourseTitle', 'CourseNumber', 'Department', 'Section', 'ScheduleType', 'Instructor', 'MeetingTime']

class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['NetId', 'FirstName', 'LastName', 'Preferred_Work_Time', 'SchoolYear', 'ContactInfo', 'OtherInfo']
