from django.http.response import HttpResponse
from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()

context={'name':'hum'}
# Create your views here.
def home(request):
     
    try:
        # intrcution pour recupere l'id dans la session
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        return render(request,"home/home.html",{"uid":uid})

    return render(request,"home/home.html",{"uid":uid}) 


