from django.shortcuts import render,HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from getplaced.models import Studtb
from getplaced.forms import StudtbForm
from getplaced.models import Student
from getplaced.forms import StudentForm
from getplaced.models import Admintb
from getplaced.forms import AdmintbForm


import requests
def first(request):
    return render(request,'welcome.html')
def login(request):
    return render(request,'login.html')

def admlogin(request):
    return render(request,'admlogin.html')

def ssignup(request):
    return render(request,'studsignup.html')



def vlogin(request):
    if request.method == "POST":
        try:
            Username=request.POST['Username']
            pwd=request.POST['pwd']
            print(Username)
            print(pwd)
            for c_users in Studtb.objects.all():
                print(str(c_users.Username))
                if str(c_users.Username)==Username:
                    login_obj=c_users
                    break
                else:
                    login_obj=None
            if login_obj is not None:
                if str(login_obj.pwd)==pwd:
                    return redirect('/admin')
                else:
                    return redirect('/vlogin')
        except:
            return HttpResponse("exception...")

def ssign(request):
    if request.method=='POST':
        username=request.POST['username']
        psd=request.POST['psd']
        form=StudentForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            c=Studtb(Username=username,pwd=psd)
            c.save()
            return redirect('/login')
    else:
        form=StudentForm()
    return render(request,'studsignup.html')

def alogin(request):
    if request.method == "POST":
        print("hii")
        try:
            print("hello")
            username=request.POST['username']
            email_id=request.POST['email_id']
            password=request.POST['password']
            for a_users in Admintb.objects.all():
                print(str(a_users.username))
                if str(a_users.username)==username  and str(a_users.email_id)==email_id:
                    print("aaa")
                    login_obj=a_users
                    break
                else:
                    login_obj=None
            if login_obj is not None:
                if str(login_obj.password)==password:
                    return redirect('/admin')
                else:
                    return redirect('/admlogin')
            return redirect('/admlogin')            
        except:
            return HttpResponse("exception...")
        







# Create your views here.
