from django.urls import path
from . import views

urlpatterns = [
    path('error/<str:netid>', views.error),
    path('home/<str:netid>/', views.query),
    path('profile/<str:netid>/', views.profile),
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('result/', views.result, name = "result")
]
