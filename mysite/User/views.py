#from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import EnrollmentForm
from .forms import CoursesForm
from .forms import LoginInfoForm
from .filters import *
from .forms import StudentsForm

# def home(request):
#     enrollments = Enrollment.objects.all()
#     return render(request, 'User/enrollment.html', {'enrollments':enrollments})

# def courses(request):
#     courses = Courses.objects.all()
#     return render(request, 'User/courses.html', {'courses':courses})

def enrollmentViewSet(request):
    enrollment_queryset = Enrollment.objects.all()
    myFilter = EnrollmentFilter(request.GET, queryset=enrollment_queryset)
    enrollment_queryset = myFilter.qs
    context = {'enrollment': enrollment_queryset, 'myFilter': myFilter}
    return render(request, 'User/enrollment.html', context)

def enrollmentCreate(request):
    form = EnrollmentForm()
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/enrollment')
    context = {'form': form}
    return render(request, 'User/forms.html', context)

def enrollmentUpdate(request, NetId, CRN):
    currentInstance =  Enrollment.objects.get(NetId = NetId, CRN = CRN)
    form = EnrollmentForm(instance=currentInstance)
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=currentInstance)
        if form.is_valid():
            form.save()
            return redirect('/enrollment')
    context = {'form': form}
    return render(request, 'User/forms.html', context)

def enrollmentDelete(request, NetId, CRN):
    currentInstance =  Enrollment.objects.get(NetId = NetId, CRN = CRN)
    if request.method == "POST":
        currentInstance.delete()
        return redirect('/enrollment')
    context = {'item': currentInstance}
    return render(request, 'User/deleteEnrollment.html', context)



def students(request):
    students = Students.objects.all()
    return render(request, 'User/students.html', {'students':students})

def StudentViewSet(request):
    myFilter = StudentsFilter(request.GET, queryset=Students.objects.all())
    context = {'myFilter': myFilter}
    return render(request, 'User/students.html', context)

def studentsCreate(request):
    form = StudentsForm()
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context = {'form': form}
    return render(request, 'User/forms.html', context)



def logininfoViewSet(request):
    logininfo_queryset = LoginInfo.objects.all()
    myFilter = LoginInfoFilter(request.GET, queryset=logininfo_queryset)
    logininfo_queryset = myFilter.qs
    context = {'logininfo': logininfo_queryset, 'myFilter': myFilter}
    return render(request, 'User/logininfo.html', context)

def logininfoCreate(request):
    form = LoginInfoForm()
    if request.method == "POST":
        form = LoginInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logininfo')

    context = {'form': form}
    return render(request, 'User/forms.html', context)

def logininfoUpdate(request, pk):
    currentInstance =  LoginInfo.objects.get(AccountName=pk)
    form = LoginInfoForm(instance=currentInstance)
    if request.method == "POST":
        form = LoginInfoForm(request.POST, instance=currentInstance)
        if form.is_valid():
            form.save()
            return redirect('/logininfo')
    context = {'form': form}
    return render(request, 'User/forms.html', context)

def logininfoDelete(request, pk):
    currentInstance =  LoginInfo.objects.get(AccountName=pk)
    if request.method == "POST":
        currentInstance.delete()
        return redirect('/logininfo')
    context = {'item': currentInstance}
    return render(request, 'User/deleteLoginInfo.html', context)



def coursesViewSet(request):
    courses_queryset = Courses.objects.all()
    myFilter = CoursesFilter(request.GET, queryset=courses_queryset)
    courses_queryset = myFilter.qs
    context = {'courses': courses_queryset, 'myFilter': myFilter}
    return render(request, 'User/courses.html', context)

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

def coursesUpdate(request, pk):
    currentInstance =  Courses.objects.get(CRN=pk)
    form = CoursesForm(instance=currentInstance)
    if request.method == "POST":
        form = CoursesForm(request.POST, instance=currentInstance)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    context = {'form': form}
    return render(request, 'User/forms.html', context)

def coursesDelete(request, pk):
    currentInstance = Courses.objects.get(CRN=pk)
    if request.method == "POST":
        currentInstance.delete()
        return redirect('/courses')
    context = {'item': currentInstance}
    return render(request, 'User/deleteCourses.html', context)








# def studentsUpdate(request, netid):
#     print("start")
#     print(netid)
#     print("end")
#     form = StudentsForm()
#     if request.method == "POST":
#         found_student = get_object_or_404(Students, NetId = netid)
#         form = StudentsForm(request.POST, found_student)
#         if form.is_valid():
#             form.save()
#             return redirect('/home')

#     context = {'form': form}
#     return render(request, 'User/forms.html', context)
