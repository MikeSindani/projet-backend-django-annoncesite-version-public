from email import message
from unicodedata import category
from webbrowser import get
from django.http import HttpResponse
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
    
    evalua = geta.get_evaluation(database,idannonce,cat)
    evalua = int(evalua)


  # -------------- siganler une annonce ---------------------
    signaler = geta.get_signaler(database,idannonce,cat)
    if signaler == True:
       message = "<p>Cet annonce a ete signaler pour divers motif(pornographique,non dans ca categorie,indesirable)</p> <p>Veillez nous aider a verifier et signaler</p> "

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
      "msg":message})
    print(data)
    cache.set('my_key', 30 , 30000000)


    return render(request,"description/description.html", {"uid":uid,
      "data":data,
      "list":list,
      "vues":nombre_de_vues,
      "titre":titre,
      "evaluation":evalua,
      "idannonce":idannonce,
      "categorie":cat,
      "msg":message})

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
      objet_mail =  "APALGREL Signale une annonce subspect :"+motif
      message_mail = autre_motif
      html_message_mail = '''
      <h1>APAGRE<strong  style="color:tomato">Lushi</strong></h1>
      <h2>ALerte Systeme</h2>
      <p>autre motif'''+autre_motif+'''</p>
      <ul>
          <li>Caterogie:'''+categorie+'''</li>
          <li>User:'''+uidannonce+'''</li>
          <li>identifiant de l'annonce:'''+str(idannonce)+'''</li>
          <li><a href="http://"></a></li>   
      </ul> 
      '''
      form_email = 'mbac3info@gmail.com'
      to_email = ['mikems@live.fr', 'mikesindani@gmail.com']
      send_mail( subject=objet_mail,message=message_mail,html_message=html_message_mail,from_email=form_email,recipient_list=to_email,fail_silently=False)

      
      
      
  reversed_url = reverse('description', kwargs={'cat':categorie, 'idannonce':idannonce})  # /another-url/123/dummy/
  return HttpResponseRedirect(reversed_url)
