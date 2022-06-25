from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()


# Create your views here.
def elevage(request):
    geta = fonction.AfficherAnnonce()
    com_list = geta.afficher_annonces_publics_categorie(database,"elevage")
    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      return render(request,"annonces/elevage.html",{"uid":uid,"com_list":com_list})
    #pagination
    page = geta.pagination_fonction(request,com_list,number_page=2)

    return render(request,"annonces/elevage.html",{"uid":uid,"com_list":page})
    
def agriculture(request):
    geta = fonction.AfficherAnnonce()
    com_list = geta.afficher_annonces_publics_categorie(database,"agriculture")
    try:
        # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        return render(request,"annonces/agriculture.html",{"uid":uid,"com_list":com_list})
    #pagination
    page = geta.pagination_fonction(request,com_list,number_page=5)

    return render(request,"annonces/agriculture.html",{"uid":uid,"com_list":page})