from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('signup/', views.signup),
    path('admins/', views.admin),
    path('users/', views.user),
    path('add_project/', views.add_project),
    path('status/', views.status),
]
