from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashbord ,name='dashbord'),
    
]