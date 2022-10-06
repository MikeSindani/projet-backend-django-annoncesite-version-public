from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
     path('app/notification/', views.notification, name="notification"),
]
