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
# Create your views here.aq
def home(request):
    geta = fonction.AfficherAnnonce()
    
     # nombre de page a afficher par paginator 
    nombre_de_page = 1
    # nombre des choix aleatoire a afficher par section 
    nombre_choix_aleatoire = 5

    try:
        # fonction pour fournir un choix aleatoire 
        list_element_categorie_agriculture = geta.description_and_home_categorie_plus(database,"agriculture")
        
        #le choix aleatoire pour le partie du site partie agriculture 
        if len(list_element_categorie_agriculture) < nombre_choix_aleatoire :
          choix_aleatoire_agriculture = random.sample(list_element_categorie_agriculture,len(list_element_categorie_agriculture))
        else:
          choix_aleatoire_agriculture = random.sample(list_element_categorie_agriculture,nombre_choix_aleatoire)
        
    except:
        choix_aleatoire_agriculture = False

    try:
        # fonction pour fournir un choix aleatoire 
        list_element_categorie_elevage = geta.description_and_home_categorie_plus(database,"elevage")
        #le choix aleatoire pour le partie du site partie elevage
        if len(list_element_categorie_elevage) < nombre_choix_aleatoire :
          choix_aleatoire_elevage = random.sample(list_element_categorie_elevage,len(list_element_categorie_elevage))
        else:
          choix_aleatoire_elevage = random.sample(list_element_categorie_elevage,nombre_choix_aleatoire)
    except:
        choix_aleatoire_elevage = False 
    
    try:
        # fonction pour fournir un choix aleatoire 
        list_data_profil_fourniseur = geta.get_data_information_user_to_homepage(database)
        #le choix aleatoire pour le partie du site partie elevage
        if len( list_data_profil_fourniseur) < nombre_choix_aleatoire :
         choix_user_profils = random.sample( list_data_profil_fourniseur,len( list_data_profil_fourniseur))
        else:
          choix_user_profils = random.sample( list_data_profil_fourniseur,nombre_choix_aleatoire)
    except:
        choix_user_profils = False 

        
    try:
        # intrcution pour recupere l'id dans la session
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        return render(request,"home/home.html",{"uid":uid,"list_elevage":choix_aleatoire_elevage,"list_agriculture":choix_aleatoire_agriculture,"list_users":choix_user_profils})

    return render(request,"home/home.html",{"uid":uid,"list_elevage":choix_aleatoire_elevage,"list_agriculture":choix_aleatoire_agriculture,"list_users":choix_user_profils})


