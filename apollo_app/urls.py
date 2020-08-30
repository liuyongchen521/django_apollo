from django.urls import path
from apollo_app import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),#添加了额首页功能
    path('safe_a/', views.safe_a),#配置访问a等级安全的路由配置
    path('safe_b/', views.safe_b),#实现了b级别的安全路由
    path('reg/', views.reg),#实现了注册的功能

]
