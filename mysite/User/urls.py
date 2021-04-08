from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('courses/',views.courses),
    path('students/', views.StudentViewSet),
    path('logininfo/', views.logininfoViewSet),
    path('createEnrollment/', views.createEnrollment, name="createEnrollment"),
    path('createCourses/', views.createCourses, name="createCourses"),
    path('logininfo_create/', views.logininfoCreate, name="logininfo_create"),
    path('students_create/', views.studentsCreate, name="students_create"),
    path('logininfo_update/<str:pk>/', views.logininfoUpdate, name='logininfo_update'),
    path('logininfo_delete/<str:pk>/', views.logininfoDelete, name='logininfo_delete')
]
