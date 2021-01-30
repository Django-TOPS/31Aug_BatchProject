from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout),
    path('updateprofile/',views.updateprofile),
    path('notfound/',views.notfound),
]
