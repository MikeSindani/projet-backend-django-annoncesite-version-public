
from datetime import date
from queue import Empty
from django.shortcuts import render
import pyrebase 
from annoncesite import fonction
from annoncesite import firebase
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse


firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()
# Create your views here.

# Create your views here.
def dashbord(request):
    choice_variable = "Home"
     # intrcution pour recupere l'id dans la session
    try:
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)
        # intruction pour recuprer le nom d'utilisateur
        userdata = geta.get_profil_data(database = database,uid = uid )
        print("HUM = " + str(userdata))   
    except:
        message = "Veillez cree Un compte ou Connectez-Vous"
        return render(request,"login/signUp.html", {"msg": message})
    # notre objet class afficher 
    com_list = geta.afficher_annonces_user_all(database,uid)
    message=" "
    try:
        page = geta.pagination_fonction(request,com_list,number_page=5)
    except:
        page = False

    # rendu de la page 
    return render(request, "dashbord/dashbord.html",{"com_list": page , "msge": message, "data": userdata,"uid":uid,"v":choice_variable})

def dashbord_favoris(request):
    choice_variable = "Favoris"
     # intrcution pour recupere l'id dans la session
    try:
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)
        # intruction pour recuprer le nom d'utilisateur
        userdata = geta.get_profil_data(database = database,uid = uid )
        print("HUM = " + str(userdata))   
    except:
        message = "Veillez cree Un compte ou Connectez-Vous"
        return render(request,"login/signUp.html", {"msg": message})
    # notre objet class afficher 
    com_list = geta.get_favoris_user_fonction(database,uid)
    message=" "
    try:
        page = geta.pagination_fonction(request,com_list,number_page=5)
    except:
        page = False

    # rendu de la page 
    return render(request, "dashbord/dashbord.html",{"com_list": page , "msge": message, "data": userdata,"uid":uid,"v":choice_variable})

def dashbord_follow(request):
    choice_variable = "follow"

     # intrcution pour recupere l'id dans la session
    try:
        geta = fonction.AfficherAnnonce()
        uid = geta.get_token(request, authe)
        # intruction pour recuprer le nom d'utilisateur
        userdata = geta.get_profil_data(database = database,uid = uid )
        print("HUM = " + str(userdata))   
    except:
        message = "Veillez cree Un compte ou Connectez-Vous"
        return render(request,"login/signUp.html", {"msg": message})


    # notre objet class afficher 
    com_list = geta.get_favoris_user_fonction(database,uid)
    message=" "
    try:
        page = geta.pagination_fonction(request,com_list,number_page=5)
    except:
        page = False

         
    # fonction pour fournir un choix aleatoire 
    list_data_profil_fourniseur = geta.get_data_information_user_to_userpage(database,uid)
    # rendu de la page 
    return render(request, "dashbord/dashbord.html",{"com_list": page , "msge": message, "data": userdata,"uid":uid,"v":choice_variable,"list_users":list_data_profil_fourniseur})


def logout(request):
    auth.logout(request)
    #geta = fonction.AfficherAnnonce()
    #com_list = geta.afficher_annonces_publics_alls(database)
    url = reverse('home')
    ret = HttpResponseRedirect(url)
    return ret

def create_annonce(request):
    from datetime import datetime, timezone , date , timedelta
    import pytz
    # la date de la publication
    tz = pytz.timezone('Europe/Berlin')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    #millis = int(time.mktime(time_now.timetuple())) #le temps qu'on a recuperer
    id_annonce = time_now.strftime('%Y%m%d%H%M%S%f')
    # ------ date de publication ------- 
    datetoday = str(date.today())
    clock = time_now.strftime('%H:%M:%S')

    # on recuper les infos du formulaires
    titre = request.POST.get("titre")
    cat = request.POST.get("cat")
    descp = request.POST.get("descp")
    produit = request.POST.get("produit")
    devise = request.POST.get("devise")
    prix = request.POST.get("prix")
    prix_min = request.POST.get("prix_min")
    prix_max = request.POST.get("prix_max")
    poids = request.POST.get("poids")
    autres = request.POST.get("autres")
    delai = request.POST.get("delai")
    quatite = request.POST.get("quatite")
    imgurl1 = request.POST.get("imgurl1")
    imgurl2 = request.POST.get("imgurl2")
    imgurl3 = request.POST.get("imgurl3")


    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce()
    uid = geta.get_token(request, authe)
    userdata = geta.get_profil_data(database,uid)

    # cacul de la date de limite de la disponibilite 
    delai = date.today() + timedelta(days = int(delai))
    delai = str(delai)

    #le dictionnaire des donnes a envoyer a firebase
    data = {
        "id_annonce":id_annonce,
        "titre": titre,
        "categorie": cat,
        "description": descp,
        "uid":uid,
        "quatite":quatite,
        "Heure" :clock,
        "date":datetoday,
        "prix":prix,
        "devise":devise,
        "prix_max":prix_max,
        "prix_min":prix_min,
        "poids":poids,
        "autres":autres,
        "delai":delai,
        "produit": produit,
        "imgurl1":imgurl1,
        "imgurl2":imgurl2,
        "imgurl3":imgurl3,
    }    
    print("date "+delai)
    #put data in the firedata base
    try:
        database.child("annonces").child(id_annonce).set(data)
        #------ on declarer meiantenant que le compte est devenu fournisseur 
        database.child("fournisseurs").child(uid).set(uid)
        database.child("utilisateurs").child(uid).child("annonces").child(id_annonce).set(data)
        if cat == "agriculture":
           database.child("categories").child(cat).child(id_annonce).set(data)
           database.child("utilisateurs").child(uid).child("categories").child(cat).child(id_annonce).set(data)
        if cat == "elevage":
           database.child("categories").child(cat).child(id_annonce).set(data)
           database.child("utilisateurs").child(uid).child("categories").child(cat).child(id_annonce).set(data)
    except:
        message = "Annonce non publies"
        url = reverse('dashbord')
        ret = HttpResponseRedirect(url)
        return ret
        #return render(request, "dashbord/dashbord.html", {"msge": message, "data": userdata})
    message = "Annonce  publies"

    # notre objet class afficher 
    com_list = geta.afficher_annonces_user_all(database,uid)
    #return render(request, "dashbord/dashbord.html", {"com_list": com_list, "msge": message, "data": userdata})
    url = reverse('dashbord')
    ret = HttpResponseRedirect(url)
    return ret

def supprimer_annonce_favoris(request,idannonce):
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce()
    uid = geta.get_token(request, authe)
    # instruction pour la suppression d'une annonce 
    try:
        database.child("utilisateurs").child(uid).child("favoris").child(idannonce).remove()
    except:
        message = "Annonce non publies"
        url = reverse('dashbord')
        ret = HttpResponseRedirect(url)
        return ret

    url = reverse('dashbord_favoris')
    ret = HttpResponseRedirect(url)
    return ret
def supprimer_annonce(request,cat,idannonce):
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce()
    uid = geta.get_token(request, authe)
    # instruction pour la suppression d'une annonce 
    try:
        database.child("annonces").child(idannonce).remove()
        database.child("Vues").child(idannonce).remove()
        database.child("avis").child("compteur").child(idannonce).remove()
        database.child("avis").child("list_avis").child(idannonce).remove()
        database.child("utilisateurs").child(uid).child("annonces").child(idannonce).remove()
        if cat == "agriculture":
           database.child("categories").child(cat).child(idannonce).remove()
           database.child("utilisateurs").child(uid).child("categories").child(cat).child(idannonce).remove()
        if cat == "elevage":
           database.child("categories").child(cat).child(idannonce).remove()
           database.child("utilisateurs").child(uid).child("categories").child(cat).child(idannonce).remove()
    except:
        message = "Annonce non publies"
        url = reverse('home')
        ret = HttpResponseRedirect(url)
        return ret

    url = reverse('dashbord')
    ret = HttpResponseRedirect(url)
    return ret
def see_favoris(request,uid,fav):
    print(uid)
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce()
    data = geta.get_favoris_user_fonction(database,uid)

    return JsonResponse({'data':data})
def suppr_follow(request,uidannonce):
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce()
    uid = geta.get_token(request, authe)
    # instruction pour la suppression d'une annonce 
    try:
        database.child("utilisateurs").child(uid).child("abonnement").child(uidannonce).remove()
    except:
        message = "Annonce non publies"
        url = reverse('home')
        ret = HttpResponseRedirect(url)
        return ret

    url = reverse('dashbord_follow')
    ret = HttpResponseRedirect(url)
    return ret