from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('contact/', views.contact ,name='contact'),
   path('contacter/', views.contacter ,name='contacter'),
   path('aboutus/', views.aboutus ,name='aboutUs'),

]
