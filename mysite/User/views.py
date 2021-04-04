#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from User.serializers import UserSerializer
from User.models import Enrollment
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import EnrollmentForm
from .forms import CoursesForm


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Enrollment.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def home(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'User/enrollment.html', {'enrollments':enrollments})

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'User/courses.html', {'courses':courses})

def logininfo(request):
    loginInfoContent = LoginInfo.objects.all()
    return render(request, 'User/logininfo.html', {'logininfo':loginInfoContent})

def createEnrollment(request):
    form = EnrollmentForm()
    if request.method == "POST":
        #print('Printing POST:', request.POST)
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return ('/home')

    context = {'form': form}
    return render(request, 'User/forms.html', context)

def createCourses(request):
    form = CoursesForm()
    if request.method == "POST":
        #print('Printing POST:', request.POST)
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return ('/home')

    context = {'form': form}
    return render(request, 'User/forms.html', context)
