import imghdr
from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
from django.http import HttpResponseRedirect
from django.urls import reverse


firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()

# Create your views here.
def signIn(request):
     try:
        # intrcution pour recupere l'id dans la session
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)   
     except:
        uid = False
        return render(request,"login/signIn.html",{"uid":uid})
   
     return render(request, "login/signIn.html",{"uid":uid})

def signUp(request):
    try:
        # intrcution pour recupere l'id dans la session
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)   
    except:
        uid = False
        return render(request,"login/signUp.html",{"uid":uid})
   
    return render(request, "login/signUp.html",{"uid":uid})

    
# pour se signup
def postsignup(request):
    #recuperer le form de signUp
    
    name = request.POST.get("name")
    prenom = request.POST.get("prenom")
    entreprise = request.POST.get("entreprise")
    tel1 = request.POST.get("tel1")
    tel2 = request.POST.get("tel2")
    whatsapp = request.POST.get("whatsapp")
    telegram = request.POST.get("telegram")
    quartier = request.POST.get("quartier")
    commune = request.POST.get("commune")
    avenue = request.POST.get("avenue")
    imgurl = request.POST.get("url")
    email = request.POST.get("email")
    passw = request.POST.get("password")


    
    #creation de l'utilisateur dans firebase
    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = "Impossible de creer un utilisateur essayer encore"
        return  render(request, "login/signUp.html", {"msg": message})

     # recupere la session 
    #session_id = user['localId']
    #request.session['uid'] = str(session_id) 
    #print("🙌🙌😂😂")
    #print(session_id)

    print("🐱‍🐉🐱‍💻🐱‍👓🐱‍🚀")
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)


    #  dictionnaire pour les donnes 
    uid = user['localId']
    data = {
            "nom": name,
            "prenom":prenom ,
            "entreprise":entreprise,
            "tel1": tel1,
            "tel2": tel2,
            "whatsapp":whatsapp,
            "telegram":telegram, 
            "avenue": avenue,
            "commune": commune,
            "quartier": quartier,
            "email":email,
            "imgurl":imgurl, 
            "statut": "1",
            "uid":uid
        }
    database.child("utilisateurs").child(uid).child("Informations").set(data)

    
    # intruction pour recuprer le nom d'utilisateur
    geta = fonction.AfficherAnnonce()
    userdata = geta.get_profil_data(database = database,uid = uid )
    print("HUM = " + str(userdata))
    message = "utilisateur a ete cree"
    # notre objet ann
    #com_list = geta.afficher_annonces_alls(database)
    #return render(request, "dashbord/dashbord.html",  { "msg": message, "data": userdata})
    url = reverse('welcome') 
    ret = HttpResponseRedirect(url)
    return ret
    

def postsignin(request):
    email = request.POST.get("email")
    passw = request.POST.get("password")

    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "mot de passe ou nom de utilisateur incorrect"
        return render(request, "login/signIn.html", {"msg": message})
    
    # recupere la session 
    print("🐱‍🐉🐱‍💻🐱‍👓🐱‍🚀")
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce()
    uid = geta.get_token(request, authe)

    # intruction pour recuprer le nom d'utilisateur
    userdata = geta.get_profil_data(database = database,uid = uid )
    print("HUM = " + str(userdata))

    # notre objet ann
    #com_list = geta.afficher_annonces_alls(database)
    # notre objet class afficher 
    com_list = geta.afficher_annonces_user_all(database,uid)
       
    #return render(request, "dashbord/dashbord.html", {"com_list": com_list,"data":userdata})
    url = reverse('dashbord') 
    ret = HttpResponseRedirect(url)
    return ret
    

def welcome(request): 
    
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce() 
    # on essayer de recupere le uid en session
    try:
         # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)
        print("😊😘😘😍😒") 
        print(uid) 
    except:
        uid = False
        return render(request,"login/signIn.html",{"uid":uid})

    # intruction pour recuprer le nom d'utilisateur
    userdata = geta.get_profil_data(database = database,uid = uid )
    
    return render(request, "login/welcome.html",  { "uid":uid,"userdata":userdata} )

def postdashbord(request):
    imgurl = request.POST.get("url")
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce() 
   
    # notre objet class afficher 
    try:
         # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)
        print("😊😘😘😍😒") 
        print(uid) 
    except:
        uid = False
        return render( request, "login/welcome.html", { "uid":uid} )
    # -------- update --------------------------
    data = {"imgurl":imgurl}   
    database.child("utilisateurs").child(uid).child("Informations").update(data)

    url = reverse('dashbord') 
    ret = HttpResponseRedirect(url)
    return ret

def passforgot(request):
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce() 
   
    # notre objet class afficher 
    try:
         # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)
        print("😊😘😘😍😒") 
        print(uid) 
    except:
        uid = False
        return render( request, "login/pass.html", { "uid":uid} )
    
    return render(request,"login/pass.html",{ "uid":uid})


def passreinitialisation(request):
    email = request.POST.get("email")
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce() 
    # reset fonction 
    authe.send_password_reset_email(email)
    # notre objet class afficher 
    try:
         # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)
        print("😊😘😘😍😒") 
        print(uid) 
    except:
        uid = False
        return render( request, "login/pass.html", { "uid":uid} )
    
    return render(request,"login/pass.html",{ "uid":uid})