from django.urls import path
from . import views

urlpatterns = [
    path('dashbord/', views.dashbord ,name='dashbord'),
    path('dashbord/favoris/', views.dashbord_favoris ,name='dashbord_favoris'),
    path('logout/', views.logout, name="logout"),
    path('creation_annonce/', views.create_annonce, name="create_annonce"),
    path('supprannonce/<str:cat>/<int:idannonce>/', views.supprimer_annonce , name="delete_annonce"),
    path('suppr_annonce_favoris/favoris/<int:idannonce>/', views.supprimer_annonce_favoris , name="delete_annonce_favoris"),
    path('get_favoris_user/<str:uid>/<str:fav>/', views.see_favoris, name="see_favoris"),
    
]