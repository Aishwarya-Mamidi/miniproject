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
    path('sviewsugg/',views.sviewsugg,name='sviewsugg'),
    path('placehis/',views.placehis,name='placehis'),
    path('viewplacehis/',views.viewplacehis,name='viewplacehis'),
    path('sviewplacehis/',views.sviewplacehis,name='sviewplacehis'),
    path('addplacedetails/',views.addplacedetails,name='addplacedetails'),
    path('viewplacedetails/',views.viewplacedetails,name='viewplacedetails'),
    path('sviewplacedetails/',views.sviewplacedetails,name='sviewplacedetails'),
    path('i/<pk>/del/',views.del_sugg,name='del_sugg'),
    path('k/<pk>/delplace/',views.del_place_details,name='del_place_details'),
    path('alogout/',views.alogout,name='alogout'),
    path('slogout/',views.slogout,name='slogout'),
    path('shome/',views.shome,name='shome'),

]