from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import CreateUserForm

def email_check(user):
    return user.username.endswith('@example.com')

def home(request):
    return render(request, 'home.html')

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
        return redirect('/home')
    data = Students.objects.raw("SELECT GROUP_CONCAT(c.CourseNumber) as result, s1.Preferred_Work_Time, s1.NetId FROM Students s1 NATURAL JOIN Enrollment e1 JOIN Courses c ON e1.CRN = c.CRN JOIN (SELECT s2.Preferred_Work_Time, e2.CRN, s2.NetId FROM Students s2 NATURAL JOIN Enrollment e2 WHERE s2.NetId = '" + netid + "') as derived WHERE e1.CRN = derived.CRN and s1.NetId <> derived.NetId GROUP by s1.NetId Order by count(e1.CRN) DESC")
    return render(request, 'query.html', {'data':data})

def profile(request, netid):
    if not (netid == request.user.username):
        return redirect('/home')
    courses = Students.objects.raw("SELECT NetId, CourseNumber FROM Enrollment NATURAL JOIN Courses WHERE NetId = '" + netid + "'")
    students = Students.objects.raw("SELECT * FROM Students WHERE NetId = '" + netid + "'")
    return render(request, 'profile.html', {'courses':courses, 'students':students})
