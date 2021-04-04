from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('courses/',views.courses),
    path('logininfo/', views.logininfo),
    path('createEnrollment/', views.createEnrollment, name="createEnrollment"),
    path('createCourses/', views.createCourses, name="createCourses")
]
