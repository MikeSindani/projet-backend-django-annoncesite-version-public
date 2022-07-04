
from unicodedata import category
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

def search(request):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()
    # rechercher code pour rechercher 
    if request.method == 'GET' and 'csrfmiddlewaretoken' in request.GET:
        search = request.GET.get("search")  
        search = str(search) 
        titre_de_la_rechercher = search
   
    # nombre de page a afficher par paginator 
    nombre_de_page = 3
    '''try: 
      com_list = cache.get('firedata')
      print("👍👍👍👍👍")
      print(com_list)
    except:'''
    
    list_element_id= geta.rechercher_fonction_dans_firebase(database,search=search)
    list_element_annonces = geta.rechercher_afficher_annonces_alls(database,list_element_id)
    print("👏👏👏👏👏👏👏👏👏👏")
    print(list_element_annonces)
    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      page = geta.pagination_fonction(request,list_element_annonces,number_page=nombre_de_page)
      content = {"uid":uid,"com_list":page,"titre":titre_de_la_rechercher}
      return render(request,"search/search.html",content)
    #pagination
    page = geta.pagination_fonction(request,list_element_annonces,number_page=nombre_de_page)

    content = {"uid":uid,"com_list":page,"titre":titre_de_la_rechercher}
    return(request,"search/search.html",content)

def searchpage(request,search):
     #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()
    # rechercher code pour rechercher
    titre_de_la_rechercher = search
   
    # nombre de page a afficher par paginator 
    nombre_de_page = 3
    '''try: 
      com_list = cache.get('firedata')
      print("👍👍👍👍👍")
      print(com_list)
    except:'''
    
    list_element_id= geta.rechercher_fonction_dans_firebase(database,search=search)
    list_element_annonces = geta.rechercher_afficher_annonces_alls(database,list_element_id)
    print("👏👏👏👏👏👏👏👏👏👏")
    print(list_element_annonces)
    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      page = geta.pagination_fonction(request,list_element_annonces,number_page=nombre_de_page)
      content = {"uid":uid,"com_list":page,"titre":titre_de_la_rechercher}
      return render(request,"search/search.html",content)
    #pagination
    page = geta.pagination_fonction(request,list_element_annonces,number_page=nombre_de_page)

    content = {"uid":uid,"com_list":page,"titre":titre_de_la_rechercher}
    return(request,"search/search.html",content)
