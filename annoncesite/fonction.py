import datetime
from imghdr import what

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
                titre = database.child("utilisateurs").child(uid).child("annonces").child(i).child("titre").get().val()
                desc = database.child("utilisateurs").child(uid).child("annonces").child(i).child("description").get().val()
                prix = database.child("utilisateurs").child(uid).child("annonces").child(i).child("prix").get().val()
                cate = database.child("utilisateurs").child(uid).child("annonces").child(i).child("categorie").get().val()
                prix_max = database.child("utilisateurs").child(uid).child("annonces").child(i).child("prix_max").get().val()
                prix_min = database.child("utilisateurs").child(uid).child("annonces").child(i).child("prix_min").get().val()
                datetoday = database.child("utilisateurs").child(uid).child("annonces").child(i).child("date").get().val()
                devise = database.child("utilisateurs").child(uid).child("annonces").child(i).child("devise").get().val()
                imgurl1 = database.child("utilisateurs").child(uid).child("annonces").child(i).child("imgurl1").get().val()
                imgurl2 = database.child("utilisateurs").child(uid).child("annonces").child(i).child("imgurl2").get().val()
                imgurl3 = database.child("utilisateurs").child(uid).child("annonces").child(i).child("imgurl3").get().val()
                id_annonce = database.child("utilisateurs").child(uid).child("annonces").child(i).get().key()
                
                data = {
                        "id":id_annonce,
                        "titre": titre,
                        "description": desc,
                        "categorie":cate,
                        "uid":uid,
                        "date":datetoday,
                        "prix":prix,
                        "devise":devise,
                        "prix_max":prix_max,
                        "prix_min":prix_min,
                        "imgurl1":imgurl1,
                        "imgurl2":imgurl2,
                        "imgurl3":imgurl3,
                    }  
                work.append(data)
            #print("liste = " + str(work))
            
            
            ''' for i in lis_time:
                i = float(i)
                dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
                data.append(dat)
            print(data)'''
            
            #com_list = zip(lis_time, work)

            return work
        else:
             return False
     def afficher_annonces_publics_cat_elevage(self, database):
        timeshamps = database.child("categories").child("elevage").shallow().get().val()
        
        if timeshamps :
            lis_time = []

            for i in timeshamps:
                lis_time.append(i)

            lis_time.sort(reverse=True)
            work = []
            #print("test = " + str(lis_time))
            data = []
            for i in lis_time:
                wor = database.child("categories").child("elevage").child(i).get().val()
                id = database.child("categories").child("elevage").child(i).child("uid").get().val()
                uidata = database.child("utilisateurs").child(id).child("Informations").get().val()
                work.append(wor)
                data.append(uidata)

            print("users id = " + str(data))
                
            #data = []
            ''' for i in lis_time:
                i = float(i)
                dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
                data.append(dat)
            print(data)'''
            # on combine le touts
            com_list = zip(lis_time,work,data)
            return com_list   
        else:
             return False
     def afficher_annonces_publics_cat_agriculture(self, database):
        timeshamps = database.child("categories").child("agriculture").shallow().get().val()
        if timeshamps :
            lis_time = []

            for i in timeshamps:
                lis_time.append(i)

            lis_time.sort(reverse=True)
            work = []
            data = []
            #print("test = " + str(lis_time))

            for i in lis_time:
                wor = database.child("categories").child("agriculture").child(i).get().val()
                id = database.child("categories").child("agriculture").child(i).child("uid").get().val()
                uidata = database.child("utilisateurs").child(id).child("Informations").get().val()
                work.append(wor)
                data.append(uidata)
                
            #print("liste = " + str(work))
                
            
            ''' for i in lis_time:
                i = float(i)
                dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M: %d-%m-%Y')
                data.append(dat)
            print(data)'''
            # on combine le touts
            com_list = zip(lis_time, work,data)
            return com_list   
        else:
             return False
       