from django.urls import path

from . import views 


urlpatterns = [path('',views.apihome,name='home')]