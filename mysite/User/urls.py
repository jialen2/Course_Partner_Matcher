from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('courses/',views.courses),
    #path('logininfo/', views.logininfo),
    path('createEnrollment/', views.createEnrollment, name="createEnrollment"),
    path('createCourses/', views.createCourses, name="createCourses"),
    path('logininfo/', views.logininfoViewSet),
    #path('create/', views.create, name="create"),
    path('logininfo_create/', views.logininfoCreate, name="logininfo_create")
]
