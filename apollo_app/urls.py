from django.urls import path
from apollo_app import views

urlpatterns = [
    path('login/', views.login),
]
