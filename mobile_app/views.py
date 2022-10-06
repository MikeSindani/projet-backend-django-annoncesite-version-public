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
def notification (request):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()
    
     # ------ generartion de liste aleatiore ---------
    list_element = geta.afficher_annonces_publics_alls(database=database)
    #  ----------- pour uid  --------------------------
    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      return render(request,"mobile/notification.html", {"uid":uid,"com_list":list_element})

    return render(request,"mobile/notification.html", {"uid":uid,"com_list":list_element})
    

    