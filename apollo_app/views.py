from django.shortcuts import render,HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("login")
def safe_a(request):
    return HttpResponse("实现了A等级的安全级别")