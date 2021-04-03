#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from User.serializers import UserSerializer
from User.models import Enrollment
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import Form


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Enrollment.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

def home(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'User/dashboard.html', {'enrollments':enrollments})

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'User/courses.html', {'courses':courses})

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
