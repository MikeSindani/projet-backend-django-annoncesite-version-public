from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('signIn/', views.signIn ,name='signIn'),
   path('signUp/', views.signUp ,name='signUp'),
]