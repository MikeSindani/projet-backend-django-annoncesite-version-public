import datetime
from imghdr import what

class AfficherAnnonce:
     def afficher_annonces_publics_alls(self, database):
            
        timeshamps_Agri = database.child("Annonces").child("Agriculture").shallow().get().val()
        timeshamps_Ele = database.child("Annonces").child("Elevage").shallow().get().val()

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
                worA = database.child("Annonces").child("Agriculture").child(i).get().val()
                if worA :
                   work.append(worA)
                worE = database.child("Annonces").child("Elevage").child(i).get().val()
                if worE :
                   work.append(worE)
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
        print("uid session 1  = " + str(a))
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
        print("nom" + nom )
        print("prenom" + prenom )
        print("uid" + uid )

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
     def afficher_annonces_alls(self, database):
        timeshamps = database.child("annonces").shallow().get().val()
        if timeshamps :
            lis_time = []

            for i in timeshamps:
                lis_time.append(i)

            lis_time.sort(reverse=True)
            work = []
            print("test = " + str(lis_time))

            for i in lis_time:
                wor = database.child("annonces").child(i).get().val()
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
        else:
             return False