from django import forms
from .models import Studtb
from .models import Student
from .models import Admintb

class StudtbForm(forms.ModelForm):
    class Meta:
        model=Studtb
        fields=['Username','pwd']
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['roll_no','studname','phoneno','email_id','branch','sec','syear','psd','username']

class AdmintbForm(forms.ModelForm):
    class Meta:
        model=Admintb
        fields=['username','email_id','password']