"""
3.Χρησιμοποιήστε το API του ΟΠΑΠ(htpps://www.opap.gr/web-servises) απο
την Python για να εμφανίσετε τα στατιστικά των αριθμών που κερδίζουν την 
πρώτη κλήρωση της ημέρας για το ΚΙΝΟ τον τρέχον μήνα.
"""
"""
Όνομα: Ηρακλής 
Επώνυμο: Τσίκας
ΑΜ : ΜΠΠΛ20082
"""

import requests
import json
from datetime import datetime

def present_data(dictio):
    rawnums=list(dictio.values())# παιρνω μονο τις λιστες με  τιμες απο την wins
    rawnums=flatten(rawnums)# και κανω ολες τις λιστες μεσα στη λιστα rawnums μια ενιαια

    for i in range(1,81):
        if rawnums.count(i) != 0:
            print("Number:"+str(i),"was found "+str(rawnums.count(i))+" times.","("+str(round(rawnums.count(i)/len(rawnums)*100))+"%)")



def flatten(list_of_lists):# συναρτηση με την οποια μετατρεπω την εμφολευμενει λιστα rawnums σε απλη λιστα
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])

def http_responce(x):
    if x != 200:
        print("Request failed for day {0}".format(i))
        print("Request failed with status: {0}".format(x))
    else:
        print("Request succeeded with status: {0}".format(x))


def draw_ids():# συνάρτηση με την οποία τραβάω απο τον ΟΠΑΠ API τα drawIDs
    
    day = datetime.today().strftime("%d")# παιρνω απο την ημερομηνια το διψηφιο της ημερας 
    month = datetime.today().strftime("%m")# παιρνω απο την ημερομηνια το διψηφιο του μηνα 
    year = datetime.today().strftime("%Y")# παιρνω απο την ημερομηνια το τετραψηφιο του χρονου 
    
    days=dict()
    if (day!='01'):# εαν στην day μεταβλητη εχει διαφορο του 01 μπαινει στο if αλλιως μπαινει στο else
        for i in range(1,int(day)+1):
            ID="https://api.opap.gr/draws/v3.0/1100/draw-date/"+str(year)+"-"+str(month)+"-" + "{:02d}".format(i) + "/"+str(year)+"-"+str(month)+"-" +"{:02d}".format(i)+"/draw-id"
            trans= requests.get(ID)
            http_responce(trans.status_code)#ελεγχω εαν υπαρχει καποιο προβλημα με το request που κανω καλοντας την συναρτηση http_responce
            htmltrans = trans.text
            days['Day'+str(i)] = json.loads(htmltrans)# αποθηκευω τα draw ids  στο dictionary  days για καθε μερα απο την πρωτη μεχρι την σημερινη
            
    else:
        # μπαινει στο else εαν στον ελεγχο του if  το day δεν ειναι διαφορο το 01
        ID="https://api.opap.gr/draws/v3.0/1100/draw-date/"+str(year)+"-"+str(month)+"-" + str(day) + "/"+str(year)+"-"+str(month)+"-" +str(day)+"/draw-id"
        trans= requests.get(ID)
        http_responce(trans.status_code)#ελεγχω εαν υπαρχει καποιο προβλημα με το request που κανω καλοντας την συναρτηση http_responce
        htmltrans = trans.text
        days['today'] = json.loads(htmltrans)# αποθηκευω τα draw ids της πρωτης ημερα
        
    return(days)

IDS=draw_ids()# καλο την συναρτηση draw_ids
url=[]
wins={}


if (len(IDS.keys())==1): # εαν το μηκος των κλειδιον το IDS ειναι ισο με 1 (δλδ ειναι η πρωτη μερα του μηνα) μπαινει στο if
    for i in range(1,len(IDS.keys())+1):   
        month=requests.get("https://api.opap.gr/draws/v3.0/1100/draw-id/"+ str(IDS['today'][0])+"/"+str(IDS['today'][0]))
        http_responce(month.status_code)#ελεγχω εαν υπαρχει καποιο προβλημα με το request που κανω καλοντας την συναρτηση http_responce
        htmlmonth=month.text
        url.append(json.loads(htmlmonth))
        for j in range (0,len(url)):# απο την λιστα url βρισκω την λιστα με τα νουμερα της πρωτης κληρωσεις της σημερινης μερας 
            wins['Day'+str(i)] = url[j]["content"][0]["winningNumbers"]["list"]
            

else:# εαν το μηκος τον κλειδιον του IDS μεγαλυτερο του 1 μπαινει στην else
    url=[]
    wins={}
    for i in range(1,len(IDS.keys())+1):
        try: # Στην περιπτωση που την σημερινη ημερα ο οπαπ δεν εχει ανεβασει κληρωση για να μην μου βγαλει error και να συνεχισει
            month=requests.get("https://api.opap.gr/draws/v3.0/1100/draw-id/"+ str(IDS['Day'+str(i)][0])+"/"+str(IDS['Day'+str(i)][0]))
            http_responce(month.status_code)#ελεγχω εαν υπαρχει καποιο προβλημα με το request που κανω καλοντας την συναρτηση http_responce
            htmlmonth=month.text
            url.append(json.loads(htmlmonth))
            for j in range (0,len(url)):# απο την λιστα url βρισκω την λιστα με τα νουμερα της πρωτης κληρωσεις για καθε μερα μεχρι σμρ
                wins['Day'+str(i)] = url[j]["content"][0]["winningNumbers"]["list"]
        except IndexError:
            print("no data for today")
            break
         
present_data(wins)# καλω την συναρτηση 

        




