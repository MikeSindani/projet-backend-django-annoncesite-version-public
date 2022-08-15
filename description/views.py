from email import message
from unicodedata import category
from webbrowser import get
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
from django.core.cache import cache
from django.urls import reverse
from django.http import HttpResponseRedirect
firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
from django.core.mail import send_mail




# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()


def description(request,cat,idannonce):
    #recuperation de la fonction appeler fonction quio est un ensemble des fonctions
    geta = fonction.AfficherAnnonce()
    #recuperation du titre 
    titre = database.child("categories").child(cat).child(idannonce).child("titre").get().val()
     #on recuperer les donnes de l'annonce 
    data = geta.description_fonction(database=database,categorie=cat,idannonce=idannonce)
    list= geta.description_and_home_categorie_plus(database,cat)
    nombre_de_vues = geta.nombres_des_vus_fonction(database=database,idannonce=idannonce)
    #text de la mise ne cache de element sur le serveur 
    
  # ------------- evaluation un produteur ---------------------------
    evalua = geta.get_evaluation(database,idannonce,cat)
    if evalua is None:
      evalua = 100
    else:
      evalua = int(evalua)


  # -------------- siganler une annonce ---------------------
    signaler = geta.get_signaler(database,idannonce,cat)
    if signaler == True:
       message = '<p>Cet annonce a ete signaler pour divers motif(pornographique,Trompe de categorie,indesirable)</p> <p style="font-weight: bold;">Veillez nous aider a verifier et signaler</p>'
    else:
       message = False


    favoris = False 
    try:
      # intrcution pour recupere l'id dans la session
      uid = geta.get_token(request, authe) 
    except:
      uid = False
      return render(request,"description/description.html", {"uid":uid,
      "data":data,
      "list":list,
      "vues":nombre_de_vues,
      "titre":titre,
      "evaluation":evalua,
      "idannonce":idannonce,
      "categorie":cat,
      "msg":message,
      "favoris": favoris
      })
    print(data)
    cache.set('my_key', 30 , 30000000)


    favoris = geta.get_favoris_fonction(database,idannonce,uid)
    if favoris is None:
      favoris = False 
    else:
      favoris = True
    
    return render(request,"description/description.html",
     {"uid":uid,
      "data":data,
      "list":list,
      "vues":nombre_de_vues,
      "titre":titre,
      "evaluation":evalua,
      "idannonce":idannonce,
      "categorie":cat,
      "msg":message,
      "favoris": favoris
      })

def evaluation(request):
  if request.method  =='POST':
      evaluation = request.POST['evaluation']
      uid = request.POST['uid']
      uidannonce = request.POST['uidannonce']
      
      print(uidannonce)
      print(evaluation)
      print(uid)

      geta = fonction.AfficherAnnonce()
      data = geta.set_evaluation_fonction(database,uid,uidannonce,evaluation)
     
  return HttpResponse(data)
def signaler(request,idannonce,uidannonce,categorie):
  # -------recuperation de la fonction appeler fonction quio est un ensemble des fonctions
  geta = fonction.AfficherAnnonce()
  
  if request.method == "GET":
      motif = request.GET.get('motif')
      autre_motif = request.GET.get('signaler-autre')

      geta.set_siganler(database,idannonce,uidannonce,categorie,motif,autre_motif)
      #-------------- preparation envoi email -------------------
      objet_mail =  "APALGREL Signale une annonce subspect :"+motif
      message_mail = autre_motif
      html_message_mail = '''
      <h1>APAGRE<strong  style="color:tomato">Lushi</strong></h1>
      <h2>Alerte Systeme</h2>
      <p>Autre motif :'''+autre_motif+'''</p>
      <ul>
          <li>Caterogie:'''+categorie+'''</li>
          <li>User:'''+uidannonce+'''</li>
          <li>identifiant de l'annonce:'''+str(idannonce)+'''</li>
          <li><a href="http://apagrel-lushi.herokuapp.com/description/'''+categorie+'''/'''+str(idannonce)+'''/">Lien</a></li>   
      </ul> 
      '''
      form_email = 'mbac3info@gmail.com'
      to_email = ['mikesindani@gmail.com']

      #-------------- envoi email -------------------
      try:
        send_mail( subject=objet_mail,message=message_mail,html_message=html_message_mail,from_email=form_email,recipient_list=to_email,fail_silently=False)
      except:
        reversed_url = reverse('description', kwargs={'cat':categorie, 'idannonce':idannonce})  # /another-url/123/dummy/
        return HttpResponseRedirect(reversed_url) 
        

      
      
      
  reversed_url = reverse('description', kwargs={'cat':categorie, 'idannonce':idannonce})  # /another-url/123/dummy/
  return HttpResponseRedirect(reversed_url)


def createCommentaire(request):
  if request.method  =='POST':
      titre_commentaire = request.POST['titre']
      desc_commentaire = request.POST['description']
      star_commentaire = request.POST['star']
      uid = request.POST['uid']
      uidannonce = request.POST['uidannonce']
      idannonce = request.POST['idannonce']
      print("-------- commentaire ---------- ")
      print(uidannonce)
      print(idannonce)
      print(uid)
      print(star_commentaire)
      print(titre_commentaire)
      print(desc_commentaire)
      #--------- on met le commentaire en faissnt appele a set_commentaitre
      geta = fonction.AfficherAnnonce()
      data = geta.set_commentaire(database,idannonce,titre_commentaire,desc_commentaire,star_commentaire,uid,uidannonce)
  return HttpResponse(data)

def commentaire(request,idannonce,num_avis):
    geta = fonction.AfficherAnnonce()
    list_avis = geta.get_commentaire(database,idannonce,num_avis)
    visible = 1
    print(idannonce)
    if request.is_ajax():
      upper = num_avis
      lower = 0
      if list_avis == False:
        list_avis = []
        size = 0
      else:
        size = len(list_avis)

      return JsonResponse({'data':list_avis[lower:upper], 'size': size})
def addfavoris(request,idannonce,uid):
    print(idannonce)
    print(uid)
    geta = fonction.AfficherAnnonce()
    data = geta.add_favoris_fonction(database,idannonce,uid)
         
    return HttpResponse(data) # Sending an success response
  
def delfavoris(request,idannonce,uid):
    print(idannonce)
    print(uid)
    geta = fonction.AfficherAnnonce()
    data = geta.del_favoris_fonction(database,idannonce,uid)

    return HttpResponse(data)
def add_follow(request,idannonce,uid):
  print(idannonce)
  print(uid)
  geta = fonction.AfficherAnnonce()
  data = geta.add_follow_fonction(database,idannonce,uid)

  return HttpResponse(data)