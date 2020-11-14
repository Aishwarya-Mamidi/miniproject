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
from getplaced.models import Suggestions
from getplaced.forms import SuggestionsForm
from getplaced.models import Placement_History
from getplaced.forms import Placement_HistoryForm
from getplaced.models import Interview_details
from getplaced.forms import Interview_detailsForm



import requests
def first(request):
    return render(request,'welcome.html')
def login(request):
    return render(request,'login.html')

def admlogin(request):
    return render(request,'admlogin.html')

def ssignup(request):
    return render(request,'studsignup.html')

def home(request):
    return render(request,'home.html')
def opensugg(request):
    return render(request,'add_sugg.html')

def viewsugg(request):
    context={
        'sugg':Suggestions.objects.all()
    }
    return render(request,'sugg_detail.html',context)

def viewplacehis(request):
    context={
        'plac':Placement_History.objects.all().order_by('-pyear')
    }
    return render(request,'viewplace_his.html',context)

def viewplacedetails(request):
    context={
        'details':Interview_details.objects.all()
    }
    return render(request,'view_place_details.html',context)
    
def vlogin(request):
    if request.method == "POST":
        try:
            Username=request.POST['Username']
            pwd=request.POST['pwd']
            print(Username)
            print(pwd)
            for c_users in Studtb.objects.all():
               # print(str(c_users.id))
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
                if str(a_users.username)==username  and str(a_users.email_id)==email_id:
                    request.session["username"]=str(a_users.username)
                    print(request.session["username"])
                    #print(a_users.id)
                    login_obj=a_users
                    break
                else:
                    login_obj=None
            if login_obj is not None:
                if str(login_obj.password)==password:
                    return redirect('/home')
                else:
                    return redirect('/admlogin')
            return redirect('/admlogin')            
        except:
            return HttpResponse("exception...")

def addsugg(request):
    if request.method=='POST':
        title=request.POST['title']
        mock_tests=request.POST['mock_tests']
        tips=request.POST['tips']
        video_links=request.POST['video_links']
        added_on=request.POST['added_on']
        added_by=request.POST['added_by']
        form=SuggestionsForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            request.session['added_by']=added_by
            return redirect('/home')
    else:
        form=StudentForm()
    return render(request,'add_sugg.html')

def placehis(request):
    if request.method=='POST':
        pyear=request.POST['pyear']
        company_name=request.POST['company_name']
        package=request.POST['package']
        ptype=request.POST['ptype']
        students_applied=request.POST['students_applied']
        students_placed=request.POST['students_placed']
        form=Placement_HistoryForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form=Placement_HistoryForm()
    return render(request,'place_his.html')

def addplacedetails(request):
    if request.method=='POST':
        company_name=request.POST['company_name']
        job_title=request.POST['job_title']
        job_description=request.POST['job_description']
        requisites=request.POST['requisites']
        selection_process=request.POST['selection_process']
        link=request.POST['link']
        time=request.POST['time']
        date=request.POST['date']
        added_by=request.POST['added_by']
        added_on=request.POST['added_on']
        form=Interview_detailsForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form=Interview_detailsForm()
    return render(request,'add_place_details.html')



    
        







# Create your views here.
