from django.db import models
from django.contrib.auth.models import User

class Admintb(models.Model):
    username=models.CharField(max_length=25,primary_key=True)
    email_id=models.EmailField(max_length=25)
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.username

class Student(models.Model):
    roll_no=models.CharField(max_length=25,primary_key=True)
    studname=models.CharField(max_length=25)
    phoneno=models.IntegerField()
    email_id=models.EmailField(max_length=25)
    branch=models.CharField(max_length=25)
    sec=models.IntegerField()
    syear=models.IntegerField()
    psd=models.CharField(max_length=25)
    username=models.CharField(max_length=25)

    def __str__(self):
        return self.roll_no
class Studtb(models.Model):
    Username=models.CharField(max_length=25,primary_key=True)
    pwd=models.CharField(max_length=25)

    def __str__(self):
        return self.Username
        
class Profile(models.Model):
    roll_no=models.ForeignKey(Student,to_field="roll_no",db_column="roll_no",on_delete=models.CASCADE)
    resume=models.FileField()
    

class Project(models.Model):
    roll_no=models.ForeignKey(Student,to_field="roll_no",db_column="roll_no",on_delete=models.CASCADE)
    project_name=models.CharField(max_length=25)
    project_des=models.CharField(max_length=25)
    tech_stack=models.CharField(max_length=25)

class Placement_history(models.Model):
    company_name=models.CharField(max_length=25)
    students_applied=models.IntegerField()
    students_placed=models.IntegerField()

    def __str__(self):
        return self.company_name

class Interview_details(models.Model):
    company_name=models.CharField(max_length=25)
    job_title=models.CharField(max_length=25)
    job_description=models.CharField(max_length=25)
    requisites=models.CharField(max_length=25)
    selection_process=models.CharField(max_length=25)

    def __str__(self):
        return self.company_name

class Suggestions(models.Model):
    mock_tests=models.URLField(max_length=200)
    tips=models.CharField(max_length=25)
    video_links=models.URLField(max_length=200)

class Register(models.Model):
    roll_no=models.ForeignKey(Student,to_field="roll_no",db_column="roll_no",on_delete=models.CASCADE)
    link=models.URLField(max_length=200)
    time=models.TimeField()
    date=models.DateField()
    place=models.CharField(max_length=25)

    
    


# Create your models here.
