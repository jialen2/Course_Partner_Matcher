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

def advanced_query_1(request):
    data = Instructors.objects.raw("SELECT I.id, I.Name, I.Department, COUNT(distinct C.CourseTitle) AS numCourses FROM Instructors I JOIN Courses C ON I.Name = C.Instructor and I.Department=C.Department GROUP BY I.Name, I.Department ORDER BY numCourses DESC;")
    return render(request, 'User/advanced_query_1.html', {'data':data})

def advanced_query_2(request):
    data = Students.objects.raw("SELECT GROUP_CONCAT(c.CourseNumber) as result, s1.Preferred_Work_Time, s1.NetId FROM Students s1 NATURAL JOIN Enrollment e1 JOIN Courses c ON e1.CRN = c.CRN JOIN (SELECT s2.Preferred_Work_Time, e2.CRN, s2.NetId FROM Students s2 NATURAL JOIN Enrollment e2 WHERE s2.NetId = 'myrah3') as derived WHERE e1.CRN = derived.CRN and s1.NetId <> derived.NetId GROUP by s1.NetId Order by count(e1.CRN) DESC")
    return render(request, 'User/advanced_query_2.html', {'data':data})

def advanced_query_3(request):
    data = Students.objects.raw("SELECT S.NetId, S.ContactInfo, S.OtherInfo, H.Department " +
                                "FROM Students S NATURAL JOIN Home H " +
                                "WHERE S.SchoolYear = 'Senior' AND H.Department IN (SELECT H1.Department FROM Home H1 WHERE H1.NetId = 'myrah3')")
    return render(request, 'User/advanced_query_3.html', {'data':data})
