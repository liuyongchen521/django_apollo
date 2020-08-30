from django.urls import path
from apollo_app import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),#添加了额首页功能

]
