from email import message
from django.shortcuts import render
import pyrebase 
from annoncesite import fonction
from annoncesite import firebase
from django.contrib import auth
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()
# Create your views here.

# Create your views here.
def dashbord(request):
     # intrcution pour recupere l'id dans la session
    try:
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)
        # intruction pour recuprer le nom d'utilisateur
        userdata = geta.get_profil_data(database = database,uid = uid )
        print("HUM = " + str(userdata))
        return render(request,"dashbord/dashbord.html",{"data": userdata})
    except:
        message = "Veillez cree Un compte ou Connectez-Vous"
        return render(request,"login/signUp.html", {"msg": message})
        

def logout(request):
    auth.logout(request)
    #geta = fonction.AfficherAnnonce()
    #com_list = geta.afficher_annonces_publics_alls(database)
    return render(request, "home/home.html")
