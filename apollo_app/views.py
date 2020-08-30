from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("login")
def index(request):
    return HttpResponse("index")
def safe_b(request):
    return HttpResponse("实现了B级别的安全等级路由")