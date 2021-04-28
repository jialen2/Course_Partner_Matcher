from django.urls import path
from . import views

urlpatterns = [
    path('error/<str:netid>', views.error),
    path('home/<str:netid>/', views.query),
    path('profile/<str:netid>/', views.profile),
    path('register/', views.registerPage, name = "register"),
    path('', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('update_profile/<str:netid>/', views.update_profile, name = "update_profile"),
    path('update_courses/', views.update_courses, name = "update_courses"),
    path('ajax/update_courses/', views.update_courses, name = "update_courses")
]
