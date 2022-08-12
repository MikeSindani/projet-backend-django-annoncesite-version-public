from datetime import datetime, timezone , date



def calculdelai(delai):
        print(delai)
        datetoday = datetime.today()
        print(datetoday)
        if str(datetoday) <= delai:
            dt_str = datetime.strptime(delai, '%Y-%m-%d')
            dt_cal = dt_str - datetoday 
            dt_cal = dt_cal.days
            if dt_cal >= 1:
                disponible = {"disponible": "Disponible pendant "+str(dt_cal)+" jours","color":"rgb(19, 196, 19)"}
            else:
                disponible = {"disponible": "Pour quelques heures","color":"tomato"}
        else:
            disponible = {"disponible": "Indisponible","color":"brown"}
        return disponible 
def calcul_moyen_pondere(database,idannonce):
    list_of_number = []
    for i in range(1,6):
       lis = database.child("avis").child("compteur").child(idannonce).child(str(i)).get().val()
       list_of_number.append(lis)
    a = (list_of_number[0]*1)+(list_of_number[1]*2)+(list_of_number[2]*3)+(list_of_number[3]*4)+(list_of_number[4]*5)
    b = list_of_number[0]+list_of_number[1]+list_of_number[2]+list_of_number[3]+list_of_number[4]
    return int(a/b)

def calcul_pourcentage_etoile_avis(database,idannonce):
    list_of_number = []
    total = database.child("avis").child("compteur").child(idannonce).child("count_total").get().val()
    for i in range(1,6):
       lis = database.child("avis").child("compteur").child(idannonce).child(str(i)).get().val()
       list_of_number.append(lis)
    for i in range(0,5):
        a = (list_of_number[i]*100)
        b = list_of_number[0]+list_of_number[1]+list_of_number[2]+list_of_number[3]+list_of_number[4]
        pourcentage = int(a/b)
        database.child("avis").child("compteur").child(idannonce).update({"pourcentage"+str(i+1):pourcentage})

