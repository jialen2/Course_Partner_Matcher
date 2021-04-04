from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('courses/',views.courses),
    path('logininfo/', views.logininfo),
    path('create/', views.create, name="create")
]
