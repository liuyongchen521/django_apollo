from django.urls import path
from apollo_app import views

urlpatterns = [
    path('login/', views.login),
    path('safe_a/', views.safe_a),#配置访问a等级安全的路由配置
]
