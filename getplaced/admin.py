from django.contrib import admin

# Register your models here.
from .models import Admintb,Student,Studtb,Project,Profile,Suggestions,Interview_details,Placement_history,Register
admin.site.register(Admintb)
admin.site.register(Student)
admin.site.register(Studtb)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Suggestions)
admin.site.register(Interview_details)
admin.site.register(Placement_history)
admin.site.register(Register)

