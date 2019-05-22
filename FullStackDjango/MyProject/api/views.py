from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Login(request):
    return HttpResponse('<h1>Login Page</h1>')

def Home(request):
    return HttpResponse('<h1>Home Page </h1>')