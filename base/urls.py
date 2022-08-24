from . import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('viewrecord/', views.viewrecord, name='viewrecord'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('bmicalculate/', views.bmicalculate, name='bmicalculate'),
    path('bmiresult/', views.bmiresult, name='bmiresult'),


]
