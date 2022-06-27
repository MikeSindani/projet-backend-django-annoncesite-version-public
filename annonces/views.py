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
def elevage(request):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()
    nombre_de_page = 3
    print("👏👏👏👏👏👏👏👏👏👏") 
    '''try: 
      com_list = cache.get('firedata')
      print("👍👍👍👍👍")
      print(com_list)
    except:'''
    com_list = geta.afficher_annonces_publics_categorie_plus(database,"elevage")
    #cache.set('firedata',com_list, 3000)
    print("❤🤣❤❤")


    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      page = geta.pagination_fonction(request,com_list,number_page=nombre_de_page)
      return render(request,"annonces/elevage.html",{"uid":uid,"com_list":page})
    #pagination
    page = geta.pagination_fonction(request,com_list,number_page=nombre_de_page)

    return render(request,"annonces/elevage.html",{"uid":uid,"com_list":page})
    
def agriculture(request):
    geta = fonction.AfficherAnnonce()
    com_list = geta.afficher_annonces_publics_categorie_plus(database,"agriculture")
    nombre_de_page = 3
    try:
        # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        #pagination
        page = geta.pagination_fonction(request,com_list,number_page=nombre_de_page)
        return render(request,"annonces/agriculture.html",{"uid":uid,"com_list":page})
    #pagination
    page = geta.pagination_fonction(request,com_list,number_page=nombre_de_page)

    return render(request,"annonces/agriculture.html",{"uid":uid,"com_list":page})