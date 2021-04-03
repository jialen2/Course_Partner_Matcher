from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('courses/',views.courses),
    path('create/', views.create, name="create")
]
