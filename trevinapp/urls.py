from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('practice/',views.fnsample,name='trevin'),
    path('trevin_api/',views.fntrevin_api,name='trevin_api'),
    path('helloworld/',views.helloworld,name='helloworld'),
    path('username/',views.saveusername,name='username'),
    path('checkpassword/',views.savepassword,name='checkpassword'),
    path('checkusername/',views.checkusername,name='checkusername')

    
]