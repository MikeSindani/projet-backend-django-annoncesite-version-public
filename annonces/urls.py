from django.urls import path
from . import views

urlpatterns = [
    path('elevage/', views.elevage ,name='elevage'),
    path('agriculture/', views.agriculture ,name='agriculture'),
    
]