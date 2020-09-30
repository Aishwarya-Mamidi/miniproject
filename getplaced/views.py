from django.shortcuts import render,HttpResponse
import requests
def first(request):
    return render(request,'welcome.html')
def login(request):
    return render(request,'login.html')

# Create your views here.
