from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
from django.core.cache import cache
import random

# configuration de firebase 
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()


# Create your views here.
def elevage(request):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()
    # nombre de page a afficher par paginator 
    nombre_de_page = 3
    print("👏👏👏👏👏👏👏👏👏👏") 
    '''try: 
      com_list = cache.get('firedata')
      print("👍👍👍👍👍")
      print(com_list)
    except:'''
    try:
        list_element_categorie = geta.afficher_annonces_publics_categorie_plus(database,"elevage")
        #cache.set('firedata',com_list, 3000)
        print("❤🤣❤❤")
        #le choix aleatoire pour le partie du site 
        if len(list_element_categorie) < 5 :
          choix_aleatoire = random.sample(list_element_categorie,len(list_element_categorie))
        else:
          choix_aleatoire = random.sample(list_element_categorie,5)
    except:
        choix_aleatoire = False
  
    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      try:
        page = geta.pagination_fonction(request,list_element_categorie,number_page=nombre_de_page)
      except:
        page = False
      return render(request,"annonces/elevage.html",{"uid":uid,"com_list":page,"list":choix_aleatoire})
    #pagination
    try:
        page = geta.pagination_fonction(request,list_element_categorie,number_page=nombre_de_page)
    except:
        page = False

    return render(request,"annonces/elevage.html",{"uid":uid,"com_list":page,"list":choix_aleatoire})
    
def agriculture(request):
    geta = fonction.AfficherAnnonce()
   
     # nombre de page a afficher par paginator 
    nombre_de_page = 3
    
    # fonction pour fournir un choix aleatoire 
    #le choix aleatoire pour le partie du site 
    try:
        list_element_categorie = geta.afficher_annonces_publics_categorie_plus(database,"agriculture")
        #cache.set('firedata',com_list, 3000)
        print("❤🤣❤❤")
        #le choix aleatoire pour le partie du site 
        if len(list_element_categorie) < 5 :
          choix_aleatoire = random.sample(list_element_categorie,len(list_element_categorie))
        else:
          choix_aleatoire = random.sample(list_element_categorie,5)
    except:
        choix_aleatoire = False
   
    try:
        # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        #pagination
        try:
          page = geta.pagination_fonction(request,list_element_categorie,number_page=nombre_de_page)
        except:
          page = False
        return render(request,"annonces/agriculture.html",{"uid":uid,"com_list":page,"list":choix_aleatoire})
    #pagination
    try:
        page = geta.pagination_fonction(request,list_element_categorie,number_page=nombre_de_page)
    except:
        page = False

    return render(request,"annonces/agriculture.html",{"uid":uid,"com_list":page,"list":choix_aleatoire})