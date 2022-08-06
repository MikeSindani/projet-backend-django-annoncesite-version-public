from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
     path('rechercher/', cache_page(60 * 15)(views.search), name="rechercher"),
     path('rechercherpage/<str:search>/',cache_page(60 * 15)(views.searchpage) , name="rechercherpage"),
     path('autosuggest/', views.autosuggest, name="autosuggest"), 
]
