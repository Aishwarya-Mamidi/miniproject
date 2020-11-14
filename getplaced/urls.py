from django.urls import path
from . import views

urlpatterns=[
    path('',views.first,name='first'),
    path('login/',views.login,name='login'),
    path('vlogin/',views.vlogin,name='vlogin'),
    path('ssignup/',views.ssignup,name='ssignup'),
    path('ssign/',views.ssign,name='ssign'),
    path('admlogin/',views.admlogin,name='admlogin'),
    path('alogin/',views.alogin,name='alogin'),
    path('home/',views.home,name='home'),
    path('opensugg/',views.opensugg,name='opensugg'),
    path('addsugg/',views.addsugg,name='addsugg'),
    path('viewsugg/',views.viewsugg,name='viewsugg'),
    path('placehis/',views.placehis,name='placehis'),
    path('viewplacehis/',views.viewplacehis,name='viewplacehis'),
    path('addplacedetails/',views.addplacedetails,name='addplacedetails'),
    path('viewplacedetails/',views.viewplacedetails,name='viewplacedetails'),

]