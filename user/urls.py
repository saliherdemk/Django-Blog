from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register,name ="register"),
    path('login/', views.login_user,name ="login"),
    path('logout/', views.logout_user,name ="logout"),
    path('dashboard/', views.dashboard,name ="dashboard"),
]

