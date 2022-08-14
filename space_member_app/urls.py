from django.urls import path
from . import views


urlpatterns = [
     path('espacemembre/<str:uidf>/',views.space_member , name="espace_membre"),
]