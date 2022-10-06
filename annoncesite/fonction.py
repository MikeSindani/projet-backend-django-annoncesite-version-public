from dataclasses import dataclass
import datetime
from imghdr import what
from itertools import product, starmap
from types import NoneType
from django.core.paginator import Paginator, EmptyPage
from django.core.cache import cache
from datetime import datetime, timezone , date

from annoncesite import sub_fonction


class AfficherAnnonce:
     
     
     def afficher_annonces_publics_alls(self, database):

        timeshamps = database.child("annonces").shallow().get().val()
        if timeshamps :
            lis_time = []
            for i in timeshamps:
                lis_time.append(i)

            
            lis_time.sort(reverse=True)
            print("test = " + str(lis_time))
            #on recupere la list
            work = []

            for i in lis_time:
                data_annnonce = database.child("annonces").child(i).get().val()
                vues = database.child("Vues").child(i).get().val()
                data_avis_annonce =  database.child("avis").child("compteur").child(i).get().val()
                id_users = database.child("annonces").child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                 
                id_annonce = {"id":i}
                #----- recuperer le delai --------
                delai =  database.child("annonces").child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)
                wor = (id_annonce,data_annnonce,data_user,vues,disponible,data_avis_annonce)
                work.append(wor)

                # --- mettre ca dans un tuple ------
                
            print("👌😁😁 " + str(work))
            print(type(work))
    
            return work
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
        print("uid session 2  = " + str(a))

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

# ------------ fontion pour prendre les annonces d'un utilisateurs dans le dashnbord -----------------
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
                vues = database.child("Vues").child(i).get().val()
                id_annonce = {"id":id_annonce} 
                data_avis_annonce =  database.child("avis").child("compteur").child(i).get().val()
                # on cree un dictionnaire pour id
                #----- recuperer le delai --------
                delai =  database.child("utilisateurs").child(uid).child("annonces").child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)
                wor = (id_annonce,data_annonce,vues,disponible,data_avis_annonce)
                work.append(wor)
                
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
                vues = database.child("Vues").child(i).get().val()
                data_avis_annonce =  database.child("avis").child("compteur").child(i).get().val()
                id_users = database.child("categories").child(cat).child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                 
                id_annonce = {"id":i}
                #----- recuperer le delai --------
                delai =  database.child("categories").child(cat).child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)
                wor = (id_annonce,data_annnonce,data_user,vues,disponible,data_avis_annonce)
                work.append(wor)

                # --- mettre ca dans un tuple ------
                
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
            print("---------------- LIST FIREBASE ------------")
            print(str(lis_time))
            #on recupere la list
            work = []

            for i in lis_time:
                data_annnonce = database.child("categories").child(cat).child(i).get().val()
                #----- recuperer uid et data users --------
                id_users = database.child("categories").child(cat).child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                id_annonce = {"id":i}

                #----- recuperer le delai --------
                delai =  database.child("categories").child(cat).child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)


                wor = (id_annonce,data_annnonce,data_user,disponible)
                work.append(wor)
                
            print("👌😁😁 " + str(work))
            print(type(work))
            return work
        else:
            return False
#----------- fonction pour recupere les donnes dans bd pour la page description -------------
     def description_fonction(seft, database,categorie,idannonce):
        work = []
        data_annnonce = database.child("categories").child(categorie).child(idannonce).get().val()
        data_avis_annonce =  database.child("avis").child("compteur").child(idannonce).get().val()
        id_users = database.child("categories").child(categorie).child(idannonce).child("uid").get().val()
        data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
         #----- recuperer le delai --------
        delai =  database.child("categories").child(categorie).child(idannonce).child("delai").get().val()
        disponible = sub_fonction.calculdelai(delai)
        wor = (data_annnonce,data_user,disponible,data_avis_annonce)
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
            # -------- update --------------------------
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
            cat = database.child("annonces").child(i).child('categorie').get().val()
            produit = database.child("annonces").child(i).child('produit').get().val()
            desc = database.child("annonces").child(i).child('description').get().val()
            uid = database.child("annonces").child(i).child('uid').get().val()
            quartier = database.child("utilisateurs").child(uid).child("Informations").child("quartier").get().val()
            avenue = database.child("utilisateurs").child(uid).child("Informations").child("avenue").get().val()
            commune = database.child("utilisateurs").child(uid).child("Informations").child("commune").get().val()
            wor = str(titre)+str(cat)+str(produit)+str(desc)+str(avenue)+str(commune)+str(quartier)+"$"+str(i)
            print("---------- work -------------")
            print(wor)
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
                vues = database.child("Vues").child(i).get().val()
                id_users = database.child("annonces").child(i).child("uid").get().val()
                data_user = database.child("utilisateurs").child(id_users).child("Informations").get().val()
                id_annonce = {"id":i}
                #----------- recupere les avis ---------------
                data_avis_annonce =  database.child("avis").child("compteur").child(i).get().val()
                # ------- affiche le delai ------------
                delai =  database.child("annonces").child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)
                wor = (id_annonce,data_annnonce,data_user,vues,disponible,data_avis_annonce)
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
                titre = database.child("annonces").child(i).child('produit').get().val()
                work.append(titre)
            cache.set('work2', work,3600)
            return work
     def set_evaluation_fonction(self,database,uid,uidannonce,evaluation):
            data = database.child("evaluation").child(uidannonce).child("list_users_evaluation").child(uid).get().val()
            print("-----------[")
            print(data)
            print("***********")
            print(evaluation)

            if data == evaluation:
                return "Vous avez deja evaluer ce producteur"

            fiable = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("fiable").get().val()
            count = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("count").get().val()       
            if fiable is  None and count is  None and data is not evaluation:
                a = {"fiable":1,"count":1,"total":100}
                database.child("evaluation").child(uidannonce).child("annonce_evaluation").set(a)
        
                # ------------- list user -------------------
                u = str(uid)
                b = {u:evaluation}
                database.child("evaluation").child(uidannonce).child("list_users_evaluation").set(b)     
              
            else:
                if evaluation == "fiable":
                    if data == "nofiable" :
                        fiable = fiable + 1
                        total = (fiable / count)*100
                        put = {"fiable":fiable,"count":count,"total":total}
                        print(put)
                        database.child("evaluation").child(uidannonce).child("annonce_evaluation").update(put)

                    else:
                        fiable = fiable + 1
                        count = count + 1
                        total = (fiable / count)*100
                        put = {"fiable":fiable,"count":count,"total":total}
                        print(put)
                        database.child("evaluation").child(uidannonce).child("annonce_evaluation").update(put)
                    # ------------- list user -------------------
                    u = str(uid)
                    b = {u:evaluation}
                    database.child("evaluation").child(uidannonce).child("list_users_evaluation").set(b)

                else:
                    if data == "fiable" :
                        count = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("count").get().val()
                        fiable = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("fiable").get().val()
                        total = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("total").get().val()
                        fiable = fiable - 1
                        total = (fiable / count)*100
                        put = {"fiable":fiable,"count":count,"total":total}
                        print(put)
                        database.child("evaluation").child(uidannonce).child("annonce_evaluation").update(put) 
                        # ------------- list user -------------------
                        u = str(uid)
                        b = {u:evaluation}
                        database.child("evaluation").child(uidannonce).child("list_users_evaluation").set(b) 
                    else:
                        count = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("count").get().val()
                        fiable = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("fiable").get().val()
                        total = database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("total").get().val()
                        count = count + 1
                        total = (fiable / count)*100
                        put = {"fiable":fiable,"count":count,"total":total}
                        print(put)
                        database.child("evaluation").child(uidannonce).child("annonce_evaluation").update(put) 
                        # ------------- list user -------------------
                        u = str(uid)
                        b = {u:evaluation}
                        database.child("evaluation").child(uidannonce).child("list_users_evaluation").set(b)

            return "Merci Pour Votre evaluation!"
     def get_evaluation(self,database,idannonce,categorie):
         uidannonce = database.child("categories").child(categorie).child(idannonce).child("uid").get().val()
         return database.child("evaluation").child(uidannonce).child("annonce_evaluation").child("total").get().val()
     def set_siganler(self,database,idannonce,uidannonce,categorie,motif,autre_motif):

        count = database.child("signaler").child("compteur").child(idannonce).child("count").get().val()
        print(type(count))
        print(count)
        if count is None:
            count1=1
            count2={"count":count1}
            data = {"idannonce":idannonce,"uiannonce":uidannonce,"categorie":categorie,"motif":motif,"autre_motif":autre_motif}
            database.child("signaler").child("compteur").child(idannonce).set(count2)
            database.child("signaler").child("list_annonces_key").child(idannonce).set(data)
        else:
            count1 = count + 1 
            count2={"count":count1}
            data = {"idannonce":idannonce,"uidannonce":uidannonce,"categorie":categorie,"motif":motif,"autre_motif":autre_motif}
            database.child("signaler").child("compteur").child(idannonce).update(count2)
            database.child("signaler").child("list_annonces_key").child(idannonce).set(data)

        if count is not None:
            if count > 200000:
                data_annonce = database.child("categories").child(categorie).child(idannonce).get().val()
                database.child("signaler").child("annonces").child(idannonce).set(data_annonce)
                database.child("categories").child(categorie).child(idannonce).remove()
                database.child("annonces").child(idannonce).remove()

            
     def get_signaler(self,database,idannonce,categorie):
        
        val = database.child("signaler").child("list_annonces_key").child(idannonce).get().val()
        print("------------key ----------------")
        print(val)
        if val is None:
            return False
        else: 
            return True

     def set_commentaire(self,database,idannonce,titre,description,star,uid,uidannonce):
        import pytz
        # la date de la publication
        tz = pytz.timezone('Europe/Berlin')
        time_now = datetime.now(timezone.utc).astimezone(tz)
        #millis = int(time.mktime(time_now.timetuple())) #le temps qu'on a recuperer
        id_commentaire = time_now.strftime('%Y%m%d%H%M%S%f')
        datetime_avis = datetime.today()
        data_avis = {
        "idannonce":idannonce,
        "titre":titre,
        "description":description,
        "star":star,
        "data_avis":str(datetime_avis),
        "uid":uid,
        "uidannonce":uidannonce,
        }
        star_str = str(star)
        data = database.child("avis").child("compteur").child(idannonce).get().val()
        if data is None:
            # --------- initilisation ------------
            dict_data_cpt = {
            "1":0,
            "2":0,
            "3":0,
            "4":0,
            "5":0,
            "count_total":0,
            "pourcentage1":0,
            "pourcentage2":0,
            "pourcentage3":0,
            "pourcentage4":0,
            "pourcentage5":0,
            "moyen":0
            }
            
            database.child("avis").child("compteur").child(idannonce).set(dict_data_cpt)
            
            # on met mettant dans la base
            count_star = 1 
            count_total = 1
            database.child("avis").child("compteur").child(idannonce).update({star_str:count_star})
            database.child("avis").child("compteur").child(idannonce).update({"count_total":count_total})
            
            #------- moyen -----------------
            moyen_pondere = sub_fonction.calcul_moyen_pondere(database,idannonce)
            database.child("avis").child("compteur").child(idannonce).update({"moyen":moyen_pondere})

            #-------- calcul pourcentage -----------------
            sub_fonction.calcul_pourcentage_etoile_avis(database,idannonce)

            # ---- code qui met le commenataire -------- 
            database.child("avis").child("list_avis").child(idannonce).child(id_commentaire).set(data_avis)
        else: 
            count = database.child("avis").child("compteur").child(idannonce).child(star_str).get().val()
            count_total = database.child("avis").child("compteur").child(idannonce).child("count_total").get().val()
            count_star = count + 1
            count_total = count_total + 1
            database.child("avis").child("compteur").child(idannonce).update({star_str:count_star})
            database.child("avis").child("compteur").child(idannonce).update({"count_total":count_total})

            #------- moyen -----------------
            moyen_pondere = sub_fonction.calcul_moyen_pondere(database,idannonce)
            database.child("avis").child("compteur").child(idannonce).update({"moyen":moyen_pondere})

            #-------- calcul pourcentage -----------------
            sub_fonction.calcul_pourcentage_etoile_avis(database,idannonce)

            # ---- code qui met le commenataire -------- 
            database.child("avis").child("list_avis").child(idannonce).child(id_commentaire).set(data_avis)
        return "Merci pour votre avis sur ce produit! "
     def get_commentaire(self,database,idannonce,num):
        timeshamps = database.child("avis").child("list_avis").child(idannonce).shallow().get().val()
        if timeshamps :
            lis_time = []
            for i in timeshamps:
                lis_time.append(i)
            
            lis_time.sort(reverse=True)
            print("------------- list de commentaire ---------------")
            print(lis_time)
            #on recupere la list
            work = []

            for i in lis_time:
                titre = database.child("avis").child("list_avis").child(idannonce).child(i).child("titre").get().val()
                desc = database.child("avis").child("list_avis").child(idannonce).child(i).child("description").get().val()
                star = database.child("avis").child("list_avis").child(idannonce).child(i).child("star").get().val()
                date = database.child("avis").child("list_avis").child(idannonce).child(i).child("data_avis").get().val()
                id_users = database.child("avis").child("list_avis").child(idannonce).child(i).child("uid").get().val()
                nom_user = database.child("utilisateurs").child(id_users).child("Informations").child("nom").get().val()
                prenom_user = database.child("utilisateurs").child(id_users).child("Informations").child("prenom").get().val()
                wor = {
                    "titre":titre,
                    "description":desc,
                    "star":star,
                    "date":date,
                    "nom":nom_user,
                    "prenom":prenom_user,
                }
                work.append(wor)
                
            print("😁😁 ")
            print(work)
            return work
        else:
            return False
     
     def add_favoris_fonction(self,database,idannonce,uid):
        database.child("utilisateurs").child(uid).child("favoris").child(str(idannonce)).set(idannonce)
        return "Cet annonce a été ajoutée à vos favoris"    
     def del_favoris_fonction(self,database,idannonce,uid):
        database.child("utilisateurs").child(uid).child("favoris").child(str(idannonce)).remove()
        return "Cet annonce a été supprimée à vos favoris"
     def get_favoris_fonction(sefl,database,idannonce,uid):
        return database.child("utilisateurs").child(uid).child("favoris").child(str(idannonce)).get().val()
     def get_favoris_user_fonction(sefl,database,uid):
        time_favoris_data = database.child("utilisateurs").child(uid).child("favoris").shallow().get().val()
        if time_favoris_data is not None:
            list_favoris_data = []
            for i in time_favoris_data:
                list_favoris_data.append(i)
            list_favoris_data.sort(reverse=True)
            print("************ list annonce favoris ****************")
            print(list_favoris_data)

            work = []
                #print("test = " + str(lis_time))
            for i in list_favoris_data:
                data_annonce= database.child("annonces").child(i).get().val()
                id_annonce = database.child("annonces").child(i).get().key()
                vues = database.child("Vues").child(i).get().val()
                data_avis_annonce =  database.child("avis").child("compteur").child(i).get().val()
                id_annonce = {"id":id_annonce}
                    # on cree un dictionnaire pour id
                    #----- recuperer le delai --------
                delai =  database.child("annonces").child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)
                wor = (id_annonce,data_annonce,vues,disponible,data_avis_annonce)
                work.append(wor)

            return work
        else:
            return False
     #---------- fonction pour prendre les users pour home -----------
     def get_data_information_user_to_homepage(self,database):
        user_data_fournisseurs = database.child("fournisseurs").shallow().get().val()
        list_fournisseurs = []
        for i in user_data_fournisseurs:
            list_fournisseurs.append(i)
        work = []
        for i in list_fournisseurs:
            user_profil_data = database.child("utilisateurs").child(i).child("Informations").get().val()
            list_uidf = {"uidf":i}
            tupl = (user_profil_data,list_uidf)
            work.append(tupl)
        return work
     def get_data_space_menber_categorie(self,database,categorie,user_id_fournisseur):
        uid = user_id_fournisseur
        cat = categorie
        timeshamps = database.child("utilisateurs").child(uid).child("categories").child(cat).shallow().get().val()
        
        if timeshamps :
            lis_time = []
            for i in timeshamps:
                lis_time.append(i)

            lis_time.sort(reverse=True)
            work = []
            #print("test = " + str(lis_time))

            for i in lis_time:
                data_annonce= database.child("utilisateurs").child(uid).child("categories").child(cat).child(i).get().val()
                id_annonce = database.child("utilisateurs").child(uid).child("categories").child(cat).child(i).get().key()
                id_annonce = {"id":id_annonce} 
                
                # on cree un dictionnaire pour id
                #----- recuperer le delai --------
                delai =  database.child("utilisateurs").child(uid).child("annonces").child(i).child("delai").get().val()
                disponible = sub_fonction.calculdelai(delai)
                wor = (id_annonce,data_annonce,disponible)
                work.append(wor)
                
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

     def add_follow_fonction(self,database,idannonce,uid):
        database.child("utilisateurs").child(uid).child("abonnement").child(str(uid)).set(idannonce)
        return "Cet annonce a été ajoutée à votre abonnement" 