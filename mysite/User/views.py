#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import EnrollmentForm
from .forms import CoursesForm
from .forms import LoginInfoForm
from .filters import LoginInfoFilter

def home(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'User/enrollment.html', {'enrollments':enrollments})

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'User/courses.html', {'courses':courses})

def logininfoViewSet(request):
    logininfo_queryset = LoginInfo.objects.all()
    myFilter = LoginInfoFilter(request.GET, queryset=logininfo_queryset)
    logininfo_queryset = myFilter.qs
    context = {'logininfo': logininfo_queryset, 'myFilter': myFilter}
    return render(request, 'User/logininfo.html', context)

def createEnrollment(request):
    form = EnrollmentForm()
    if request.method == "POST":
        #print('Printing POST:', request.POST)
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {'form': form}
    return render(request, 'User/forms.html', context)

def createCourses(request):
    form = CoursesForm()
    if request.method == "POST":
        #print('Printing POST:', request.POST)
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {'form': form}
    return render(request, 'User/forms.html', context)

def logininfoCreate(request):
    form = LoginInfoForm()
    if request.method == "POST":
        form = LoginInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logininfo')

    context = {'form': form}
    return render(request, 'User/forms.html', context)
