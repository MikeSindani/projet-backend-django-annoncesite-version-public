from django.urls import path
from . import views

urlpatterns = [
     path('description/<str:cat>/<int:idannonce>/', views.description, name="description"), 
     path('evaluation/', views.evaluation, name="evaluation"),
     path('create_commentaire/', views.createCommentaire, name="create_commentaire"),
     path('signaler_annonce/<int:idannonce>/<str:uidannonce>/<str:categorie>/', views.signaler, name="signaler"), 
     path('get_commentaire/<int:idannonce>/<int:num_avis>/', views.commentaire, name='getcommentaire'), 
]