from django.http.response import HttpResponse
from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
import random

firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()

context={'name':'hum'}
# Create your views here.
def home(request):
    geta = fonction.AfficherAnnonce()
    list_element_categorie_agriculture = geta.afficher_annonces_publics_categorie_plus(database,"agriculture")
    list_element_categorie_elevage = geta.afficher_annonces_publics_categorie_plus(database,"elevage")
     # nombre de page a afficher par paginator 
    nombre_de_page = 1
    # nombre des choix aleatoire a afficher par section 
    nombre_choix_aleatoire = 6
    
    # fonction pour fournir un choix aleatoire 
    #le choix aleatoire pour le partie du site partie agriculture 
    if len(list_element_categorie_agriculture) < 5 :
      choix_aleatoire_agriculture = random.sample(list_element_categorie_agriculture,len(list_element_categorie_agriculture))
    else:
       choix_aleatoire_agriculture = random.sample(list_element_categorie_agriculture,nombre_choix_aleatoire)
    #le choix aleatoire pour le partie du site partie elevage
    if len(list_element_categorie_elevage) < 5 :
      choix_aleatoire_elevage = random.sample(list_element_categorie_elevage,len(list_element_categorie_elevage))
    else:
      choix_aleatoire_elevage = random.sample(list_element_categorie_elevage,nombre_choix_aleatoire)
     
    try:
        # intrcution pour recupere l'id dans la session
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        return render(request,"home/home.html",{"uid":uid,"list_elevage":choix_aleatoire_elevage,"list_agriculture":choix_aleatoire_agriculture})

    return render(request,"home/home.html",{"uid":uid,"list_elevage":choix_aleatoire_elevage,"list_agriculture":choix_aleatoire_agriculture}) 


