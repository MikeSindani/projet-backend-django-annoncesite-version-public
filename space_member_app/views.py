from django.shortcuts import render

from unicodedata import category
from django.http import JsonResponse
from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
from django.core.cache import cache
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()
# Create your views here.
def space_member(request,uidf):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()

    user_profil = geta.get_profil_data(database, uidf)
    list_elevage = geta.get_data_space_menber_categorie (database,"elevage",uidf)
    list_agriculture = geta.get_data_space_menber_categorie(database,"agriculture",uidf)


    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      content = {"uid":uid,"list_elevage":list_elevage,"list_agriculture":list_agriculture,"user_profil":user_profil}
      return render(request,"space/space_member.html",content)

    content = {"uid":uid,"list_elevage":list_elevage,"list_agriculture":list_agriculture,"user_profil":user_profil}
    return render(request,"space/space_member.html",content)