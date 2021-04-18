from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerPage),
    path('home/<str:netid>/', views.query),
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('result/', views.result, name = "result")
]
