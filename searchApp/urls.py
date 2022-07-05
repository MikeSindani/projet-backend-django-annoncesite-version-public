from django.urls import path
from . import views

urlpatterns = [
     path('rechercher/', views.search, name="rechercher"),
     path('rechercherpage/<str:search>/', views.searchpage, name="rechercherpage"),
     path('autosuggest/', views.autosuggest, name="autosuggest"), 
]