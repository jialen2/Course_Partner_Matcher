#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import Form, LoginInfoForm


def home(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'User/dashboard.html', {'enrollments':enrollments})

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'User/courses.html', {'courses':courses})

def logininfoViewSet(request):
    logininfo_queryset = LoginInfo.objects.all()
    return render(request, 'User/logininfo.html', {'logininfo':logininfo_queryset})

def create(request):
    form = Form()
    if request.method == "POST":
        #print('Printing POST:', request.POST)
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return ('/home')

    context = {'form': form}
    return render(request, 'User/forms.html', context)

def logininfoCreate(request):
    form = LoginInfoForm()
    if request.method == "POST":
        form = LoginInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return('/logininfo')

    context = {'form': form}
    return render(request, 'User/logininfo_forms.html', context)
