from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollmentViewSet),
    path('enrollment/', views.enrollmentViewSet),
    path('enrollment_create/', views.enrollmentCreate, name="enrollment_create"),
    path('enrollment_update/<str:NetId>/<str:CRN>', views.enrollmentUpdate, name="enrollment_update"),
    path('enrollment_delete/<str:NetId>/<str:CRN>', views.enrollmentDelete, name="enrollment_delete"),

    path('courses/', views.coursesViewSet),
    path('createCourses/', views.createCourses, name="createCourses"),
    path('courses_update/<str:pk>/', views.coursesUpdate, name='courses_update'),
    path('courses_delete/<str:pk>/', views.coursesDelete, name='courses_delete'),

    path('students/', views.StudentViewSet),
    path('students_create/', views.studentsCreate, name="students_create"),
    path('students_query/', views.enrollment_advanced_query),

    path('logininfo/', views.logininfoViewSet),
    path('logininfo_create/', views.logininfoCreate, name="logininfo_create"),
    path('logininfo_update/<str:pk>/', views.logininfoUpdate, name='logininfo_update'),
    path('logininfo_delete/<str:pk>/', views.logininfoDelete, name='logininfo_delete'),

]
