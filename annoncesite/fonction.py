from dataclasses import dataclass
import datetime
from imghdr import what
from itertools import product
from django.core.paginator import Paginator, EmptyPage
from django.core.cache import cache


class AfficherAnnonce:
     def afficher_annonces_publics_alls(self, database):
            
        timeshamps= database.child("Annonces").shallow().get().val()
        lis_time = []
        for i in timeshamps:
            lis_time.append(i)

        lis_time.sort(reverse=True)
        print("test = " + str(lis_time))

        work = []

        for i in lis_time:
            wor = database.child("Annonces").child(i).get().val()

        work.append(wor)
        print("test2 = " + str(work))

        data = []

        for i in lis_time:
            i = float(i)
            dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
            data.append(dat)

            print(data)
            # on combine le touts
            com_list = zip(lis_time, data, work)
            return com_list
        return False
     def afficher_annonces_profil(self, database,uid):
        
        timeshamps_Agri = database.child("utilisateurs").child(uid).child("Annonces").child("Agriculture").shallow().get().val()
        timeshamps_Ele = database.child("utilisateurs").child(uid).child("Annonces").child("Elevage").shallow().get().val()

        if timeshamps_Agri or timeshamps_Ele:
            lis_time = []
            if timeshamps_Agri :
                for i in timeshamps_Agri:
                    lis_time.append(i)
            if timeshamps_Ele :
                for i in timeshamps_Ele:
                    lis_time.append(i)

            lis_time.sort(reverse=True)
            print("test = " + str(lis_time))
            work = []
            for i in lis_time:
                worA = database.child("utilisateurs").child(uid).child("Annonces").child("Agriculture").child(i).get().val()
                if worA :
                   work.append(worA)
                worE = database.child("utilisateurs").child(uid).child("Annonces").child("Elevage").child(i).get().val()
                if worE :
                   work.append(worE)
            print("test2 = " + str(work))

            data = []

            for i in lis_time:
                i = float(i)
                dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
                data.append(dat)

            print("test3 = "+ str(data))
            # on combine le touts
            com_list = zip(lis_time, data, work)
            return com_list
        return False
     def get_token(self, request,authe):

        # intrcution pour recupere l'id dans la session
        idtoken = request.session['uid']
        a = authe.get_account_info(idtoken)
        a = a["users"]
        #print("uid session 1  = " + str(a))
        a = a[0]
        a = a["localId"]
        #print("uid session 2  = " + str(a))

        return a
     def get_profil_data(self,database,uid):

        # recuperer les donnes de firebase 
        nom = database.child("utilisateurs").child(uid).child('Informations').child('nom').get().val()
        prenom = database.child("utilisateurs").child(uid).child('Informations').child('prenom').get().val()
        imgurl = database.child("utilisateurs").child(uid).child('Informations').child('imgurl').get().val()
        email = database.child("utilisateurs").child(uid).child('Informations').child('email').get().val()
        adr = database.child("utilisateurs").child(uid).child('Informations').child('adr').get().val()
        tel1 = database.child("utilisateurs").child(uid).child('Informations').child('tel1').get().val()
        tel2 = database.child("utilisateurs").child(uid).child('Informations').child('tel2').get().val()
        uidFirebase = database.child("utilisateurs").child(uid).child('Informations').child('uid').get().val()
        telegram = database.child("utilisateurs").child(uid).child('Informations').child('telegram').get().val()
        whatsapp = database.child("utilisateurs").child(uid).child('Informations').child('whatsapp').get().val()
        entreprise = database.child("utilisateurs").child(uid).child('Informations').child('entreprise').get().val()
        # verifeir c'est donnes 
        #print("nom" + nom )
        #print("prenom" + prenom )
        #print("uid" + uid )

        # mettre ca dans une base de donnes 

        data = {
            "nom" : nom,
            "prenom" : prenom,
            "email" : email,
            "adr" : adr,
            "tel1": tel1,
            "tel2": tel2,
            "imgurl":imgurl,
            "uidFirebase" : uidFirebase,
            "telegram" : telegram,
            "whatsapp" : whatsapp,
            "entreprise" : entreprise
        }
        # rendre les dictionnaires 
        return data
     def afficher_annonces_user_all(self, database,uid):
        timeshamps = database.child("utilisateurs").child(uid).child("annonces").shallow().get().val()
        if timeshamps :
            lis_time = []
            for i in timeshamps:
                lis_time.append(i)

            lis_time.sort(reverse=True)
            work = []
            #print("test = " + str(lis_time))

            for i in lis_time:
                data_annonce= database.child("utilisateurs").child(uid).child("annonces").child(i).get().val()
                id_annonce = database.child("utilisateurs").child(uid).child("annonces").child(i).get().key()
                vue = database.child("vues").child(i).get().val()
                id_annonce = {"id":id_annonce} # on cree un dictionnaire pour id
                data = (id_annonce,data_annonce,vue)# on cree un tuple 
                work.append(data)# on met le tuple dans la liste
            print("terminer 👍")
            #print("liste = " + str(work))
            '''
            d = database.child("categories").order_by_child("elevage").limit_to_first(2).get()
            print(d)
            for i in lis_time:
                i = float(i)
                dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
                data.append(dat)
            print(data)'''
            
            #com_list = zip(lis_time, work)

            return work
        else:
             return False
     def afficher_annonces_publics_categorie(self, database,cat):

        timeshamps = database.child("categories").child(cat).shallow().get().val() 
        if timeshamps :
            # on cree la liste 
            lis_time = []
            #ON MET LES ELEMENTS DE TIMESHMPS DANS LA LISTE
            for i in timeshamps:
                lis_time.append(i)
            #ON ORDRONNE LA LISTE 
            lis_time.sort(reverse=True)
            work = []
            #print("test = " + str(lis_time))
            data = []
            for i in lis_time:
                # on recupere les valeurs precis ayant besoin afin de constituer un dictionnaire
                id_annonce = database.child("categories").child(cat).child(i).get().key()
                id_users = database.child("categories").child(cat).child(i).child("uid").get().val()
                titre = database.child("categories").child(cat).child(i).child("titre").get().val()
                desc = database.child("categories").child(cat).child(i).child("description").get().val()
                prix = database.child("categories").child(cat).child(i).child("prix").get().val()
                cate = database.child("categories").child(cat).child(i).child("categorie").get().val()
                prix_max = database.child("categories").child(cat).child(i).child("prix_max").get().val()
                prix_min = database.child("categories").child(cat).child(i).child("prix_min").get().val()
                datetoday = database.child("categories").child(cat).child(i).child("date").get().val()
                devise = database.child("categories").child(cat).child(i).child("devise").get().val()
                imgurl1 =database.child("categories").child(cat).child(i).child("imgurl1").get().val()
                imgurl2 = database.child("categories").child(cat).child(i).child("imgurl2").get().val()
                imgurl3 = database.child("categories").child(cat).child(i).child("imgurl3").get().val()
                # on recupere la personne ayant publier l'annonce son nom et prenom 
                user_name = database.child("utilisateurs").child(id_users).child("Informations").child("nom").get().val()
                user_prenom = database.child("utilisateurs").child(id_users).child("Informations").child("prenom").get().val()
                user_adresse = database.child("utilisateurs").child(id_users).child("Informations").child("adr").get().val()
                data = {
                        "id":id_annonce,
                         "titre": titre,
                        "description": desc,
                        "categorie":cate,
                        "date":datetoday,
                        "prix":prix,
                        "devise":devise,
                        "prix_max":prix_max,
                        "prix_min":prix_min,
                        "imgurl1":imgurl1,
                        "imgurl2":imgurl2,
                        "imgurl3":imgurl3,
                        "nom":user_name,
                        "prenom":user_prenom,
                        "adr":user_adresse
                    }  
                work.append(data)
                

            #print("users id = " + str(data))
                
            #data = []
            ''' for i in lis_time:
                i = float(i)
                dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
                data.append(dat)
            print(data)'''
            # on combine le touts
            #com_list = zip(lis_time,work,data)
            return work  
        else: 
            return False
     def pagination_fonction(self,request,list,number_page):
         # pagination 
        
        p = Paginator(list,number_page)
        print("NUMBER DES PAGES ")
        print(p.num_pages)

        #prendre la page de l'url 
        page_num = request.GET.get("page",1)
        print("1")
        try:
            page = p.page(page_num)
            print("2")
        except EmptyPage:
            page = p.page(1)
            print("3")
            return page
        return page
     def afficher_annonces_publics_categorie_plus(self, database,cat):
        
        timeshamps = database.child("categories").child(cat).shallow().get().val()
        if timeshamps :
            lis_time = []
            for i in timeshamps:
                lis_time.append(i)
            lis_time.sort(reverse=True)
            print("test = " + str(lis_time))
            #on recupere la list
            work = []

            for i in lis_time:
                data_annnonce = database.child("categories").child(cat).child(i).get().val()
                id_users = database.child("categories").child(cat).child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                id_annonce = {"id":i}
                wor = (id_annonce,data_annnonce,data_user)
                work.append(wor)
            print("👌😁😁 " + str(work))
            print(type(work))
    
            return work
        return False
     def description_and_home_categorie_plus(self, database,cat):
        
        timeshamps = database.child("categories").child(cat).shallow().get().val()
        if timeshamps :
            lis_time = []
            for i in timeshamps:
                a=0
                a=a+1
                lis_time.append(i)
                if a == 10:
                    break

            lis_time.sort(reverse=True)
            print("test = " + str(lis_time))
            #on recupere la list
            work = []

            for i in lis_time:
                data_annnonce = database.child("categories").child(cat).child(i).get().val()
                id_users = database.child("categories").child(cat).child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                id_annonce = {"id":i}
                wor = (id_annonce,data_annnonce,data_user)
                work.append(wor)
            print("👌😁😁 " + str(work))
            print(type(work))
    
            return work
        return False
     def description_fonction(seft, database,categorie,idannonce):
         work = []
         data_annnonce = database.child("categories").child(categorie).child(idannonce).get().val()
         id_users = database.child("categories").child(categorie).child(idannonce).child("uid").get().val()
         data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
         wor = (data_annnonce,data_user)
         work.append(wor)
         return work

     def nombres_des_vus_fonction(self,database,idannonce):
          get_data = database.child("Vues").child(idannonce).get().val()
          print(get_data)
          if get_data is None :       
              a = 0
              a=a+1
              data = {"count":a}    
              set_data = database.child("Vues").child(idannonce).set(data)
          else:
              get_data = database.child("Vues").child(idannonce).get().val()
              a = int(get_data["count"])
              a = a+1
              data = {"count":a}   
              database.child("Vues").child(idannonce).update(data) 
          get_data = database.child("Vues").child(idannonce).get().val()
          print(get_data)
          return get_data
     def rechercher_fonction_dans_firebase(self,database,search):

        search = search.lower()  

        timestamps = database.child("annonces").shallow().get().val()
        print("😎😎😎😎😎😎😎")
        print(type(timestamps))
            
        work_id=[]
        for i in timestamps:
            titre = database.child("annonces").child(i).child('titre').get().val()
            cat = database.child("annonces").child(i).child('categories').get().val()
            produit = database.child("annonces").child(i).child('produit').get().val()
            desc = database.child("annonces").child(i).child('description').get().val()
            wor = str(titre)+str(cat)+str(produit)+str(desc)+"$"+str(i)
            work_id.append(wor)

        matching = [str(string) for string in work_id if search in string.lower()]
        s_work=[]
        s_id=[]
        for i in matching:
          part_text,part_ids=i.split("$")
          s_work.append(part_text)
          s_id.append(part_ids)

        return s_id
     def rechercher_afficher_annonces_alls(self,database,listannonce):
        
            listannonce.sort(reverse=True)
            print("test = " + str(listannonce))
            #on recupere la list
            work = []
            for i in listannonce:
                data_annnonce = database.child("annonces").child(i).get().val()
                id_users = database.child("annonces").child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                id_annonce = {"id":i}
                wor = (id_annonce,data_annnonce,data_user)
                work.append(wor)
            #print("👌😁😁 " + str(work))
            #print(type(work))
    
            return work
     def autosuggest_firebase_direct(self,database):
        work=[]
        if cache.get('work2') is not None: 
            work = cache.get('work2')
            print(work)
            print("CACHED")
            return work
        else:
            work=[]
            #recuperation des cles 
            timestamps = database.child("annonces").shallow().get().val()
            print("😎😎😎😎😎😎😎")
            print(timestamps)
        # on recuperer cle par cle 
            for i in timestamps:
                titre = database.child("annonces").child(i).child('titre').get().val()
                work.append(titre)
            cache.set('work2', work,3600)
            return work

       

              