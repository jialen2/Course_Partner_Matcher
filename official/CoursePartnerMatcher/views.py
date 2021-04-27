from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection

from .models import *
from .forms import *

import random

from .image import header

def email_check(user):
    return user.username.endswith('@example.com')

def error(request, netid):
    return render(request, 'error.html', {'netid':netid})

def result(request):
    return render(request, 'main.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/home/' + request.user.username)
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('/login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/' + username)
            else:
                messages.info(request, 'Username or Password not correct')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
def query(request, netid):
    if not (netid == request.user.username):
        return redirect('/error/' + netid)
    data = Students.objects.raw("SELECT GROUP_CONCAT(c.CourseNumber) as result, s1.Preferred_Work_Time, s1.NetId FROM Students s1 NATURAL JOIN Enrollment e1 JOIN Courses c ON e1.CRN = c.CRN JOIN (SELECT s2.Preferred_Work_Time, e2.CRN, s2.NetId FROM Students s2 NATURAL JOIN Enrollment e2 WHERE s2.NetId = '" + netid + "') as derived WHERE e1.CRN = derived.CRN and s1.NetId <> derived.NetId GROUP by s1.NetId Order by count(e1.CRN) DESC")
    courses = Students.objects.raw("SELECT NetId, CourseNumber FROM Enrollment NATURAL JOIN Courses WHERE NetId = '" + netid + "'")
    return render(request, 'query.html', {'data':data, 'courses':courses})



def profile(request, netid):
    if not (netid == request.user.username):
        return redirect('/error/' + netid)
    header_list = random.choice(header)
    courses = Students.objects.raw("SELECT NetId, CourseNumber FROM Enrollment NATURAL JOIN Courses WHERE NetId = '" + netid + "'")
    students = Students.objects.raw("SELECT * FROM Students WHERE NetId = '" + netid + "'")
    student_name = ""
    for student in students:
        student_name = student.FirstName + " " + student.LastName
    course_list = ""
    for i in courses:
        course_list += i.CourseNumber + ", "
    course_list = course_list[0: len(course_list) - 2]
    cursor = connection.cursor()
    arg = [netid]
    cursor.callproc('result', arg)
    status = cursor.fetchone()[1]
    return render(request, 'profile.html', {'courses':course_list, 'students':students, 'student_name': student_name, "status": status, "header_list": header_list})

def update_courses(request):
    netid = request.POST.get('NetId')
    courses = request.POST.getlist('courses[]')
    currentInstance = Enrollment.objects.filter(NetId=netid)
    for i in currentInstance:
        tmp = Courses.objects.raw("SELECT CRN, CourseNumber FROM Courses WHERE CRN = " + i.CRN)
        for j in tmp:
            if j.CourseNumber not in courses:
                foundInstance = Enrollment.objects.get(NetId=netid, CRN = i.CRN)
                foundInstance.delete()
            else:
                courses.remove(j.CourseNumber)
    for i in courses:
        tmp = Courses.objects.raw("SELECT c.CRN FROM Courses c WHERE c.CourseNumber = '" + i + "' LIMIT 1;")
        for j in tmp:
            toAdd = {'NetId': netid, 'CRN': j.CRN}
            form = EnrollmentForm(toAdd)
            if form.is_valid():
                form.save()
    return redirect('/profile/' + netid)

def update_profile(request, netid):
    courses = Students.objects.raw("SELECT NetId, CourseNumber FROM Enrollment NATURAL JOIN Courses WHERE NetId = '" + netid + "'")
    students = Students.objects.raw("SELECT * FROM Students WHERE NetId = '" + netid + "'")
    student_name = ""
    for student in students:
        student_name = student.FirstName + " " + student.LastName
        first_name = student.FirstName
        last_name = student.LastName
    currentInstance = Students.objects.get(NetId=netid)
    form = StudentsForm(instance=currentInstance)
    if request.method == "POST":
        toUpdate = request.POST.copy()
        toUpdate['NetId'] = currentInstance.NetId
        toUpdate['OtherInfo'] = currentInstance.OtherInfo
        form = StudentsForm(toUpdate, instance=currentInstance)
        if form.is_valid():
            form.save()
            return redirect('/profile/' + netid)
    curr_course = []
    course_list = ""
    for i in courses:
        curr_course.append(i.CourseNumber)
        course_list += i.CourseNumber + ", "
    course_list = course_list[0: len(course_list) - 2]
    tmp = Courses.objects.raw("SELECT distinct CRN, CourseNumber FROM Courses")
    year_list = ['freshman', 'sophomore', 'junior', 'senior', 'masters', 'PhD']
    time_list = ['early morning', 'morning', 'noon', 'afternoon', 'evening', 'late night']
    curr_year = currentInstance.SchoolYear
    curr_time = currentInstance.Preferred_Work_Time
    for i in year_list:
        if i == curr_year:
            year_list.remove(i)
    for j in time_list:
        if j == curr_time:
            time_list.remove(j)
    all_courses = []
    for i in tmp:
        if i.CourseNumber not in all_courses and i.CourseNumber not in curr_course:
            all_courses.append(i.CourseNumber)
    return render(request, 'update_profile.html', {'courses':course_list, 'students':students, 'student_name': student_name, 'first_name': first_name, 'last_name': last_name, 'all_courses': all_courses, 'form':form, 'year_list': year_list, 'time_list': time_list, 'curr_year': curr_year, 'curr_time': curr_time, 'curr_course': curr_course})
