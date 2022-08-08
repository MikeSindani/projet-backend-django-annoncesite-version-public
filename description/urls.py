from django.urls import path
from . import views

urlpatterns = [
     path('description/<str:cat>/<int:idannonce>/', views.description, name="description"), 
     path('evaluation/', views.evaluation, name="evaluation"),  
]