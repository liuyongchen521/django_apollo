from django.urls import path
from apollo_app import views

urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),#添加了额首页功能
    path('safe_a/', views.safe_a),#配置访问a等级安全的路由配置
]
