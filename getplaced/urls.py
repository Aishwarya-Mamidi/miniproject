from django.urls import path
from . import views

urlpatterns=[
    path('',views.first,name='first'),
    path('login/',views.login,name='login'),
    path('vlogin/',views.vlogin,name='vlogin'),
    path('ssignup/',views.ssignup,name='ssignup'),
    path('ssign/',views.ssign,name='ssign'),




]