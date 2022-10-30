from django.shortcuts import render
import pyrebase
from annoncesite import fonction
from annoncesite import firebase
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

firebase_app = pyrebase.initialize_app(firebase.firebaseConfig)
# Get a reference to the auth service
authe = firebase_app.auth()
database = firebase_app.database()

# Create your views here.
def contact(request):
    
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce() 
    # reset fonction 
    
    # notre objet class afficher 
    try:
         # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)
        print("😊😘😘😍😒") 
        print(uid) 
    except:
        uid = False
        return render(request,"contact/contact.html",{ "uid":uid})
    
    return render(request,"contact/contact.html",{ "uid":uid})


def contacter(request):
    nom = request.POST.get("nom")
    objet = request.POST.get("objet")
    email = request.POST.get("email")
    msg = request.POST.get("message")
    # intrcution pour recupere l'id dans la session
    geta = fonction.AfficherAnnonce() 
    # reset fonction 
    objet_mail =  "APALGREL un client Souhaite Vous contacter :"
    message_mail = "Client contact"
    html_message_mail = '''
      <h1>APAGRE<strong  style="color:tomato">Lushi</strong></h1>
      <h2>Contacter d'utilisateur</h2>
      <ul>
          <li>Nom:'''+nom+'''</li>
          <li>Objet: '''+objet+'''</li>
          <li><a href="'''+email+'''">'''+email+'''</a></li>   
      </ul> 
      <p> <strong>Message</strong> </p>
      <p>'''+msg+'''</p>
      '''
    form_email = 'mbac3info@gmail.com'
    to_email = ['mikesindani@gmail.com']

      #-------------- envoi email -------------------
    try:
        send_mail( subject=objet_mail,message=message_mail,html_message=html_message_mail,from_email=form_email,recipient_list=to_email,fail_silently=False)
    except:
        reversed_url = reverse('contact')  # /another-url/123/dummy/
        return HttpResponseRedirect(reversed_url) 
    
    reversed_url = reverse('home')  # /another-url/123/dummy/
    return HttpResponseRedirect(reversed_url)

def aboutus(request):
    geta = fonction.AfficherAnnonce() 
    # reset fonction 
    
    # notre objet class afficher 
    try:
         # intrcution pour recupere l'id dans la session
        uid = geta.get_token(request, authe)
        print("😊😘😘😍😒") 
        print(uid) 
    except:
        uid = False
        return render(request,"aproposde/aproposde.html",{ "uid":uid})
    
    return render(request,"aproposde/aproposde.html",{ "uid":uid})
  