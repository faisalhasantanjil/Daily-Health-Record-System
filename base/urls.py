from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

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
    path('addhealthinfo/', views.addhealthinfo, name='addhealthinfo'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
