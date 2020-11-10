from django import forms
from .models import Studtb
from .models import Student

class StudtbForm(forms.ModelForm):
    class Meta:
        model=Studtb
        fields=['Username','pwd']
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['roll_no','studname','phoneno','email_id','branch','sec','syear','psd','username']