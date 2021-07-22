"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου
και μετατρέπει τον κάθε χαρακτήρα στον αντίστοιχο αριθμό ASCII και κρατάει τους μονούς. 
Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος με “μπάρες” χρησιμοποιώντας το χαρακτήρα *, 
όπου κάθε * αντιστοιχεί σε 1%. Η στρογγυλοποίηση θα γίνει προς τα πάνω.
"""
"""
Όνομα: Ηρακλής 
Επώνυμο: Τσίκας
ΑΜ : ΜΠΠΛ20082
"""
import re
import sys
import os

def parse_file():
    
    text=x.read()
    text=re.sub('[^A-Za-z0-9 ]+', '', text)#αντικαθιστω με κενα οπου υπαρχει [, . !? "" () και την αλλαγη γραμμης]
    text_ascii = text.split(" ")# οπου υπαρχει κενο κανω split
    return (text_ascii)

try:# ελεγχει εαν ο χρηστης φορτωνει αρχειο
    file_in=sys.argv[1]
except IndexError as e:
    print("File in not provided")
    file_in = "sampletext.txt"
else:
    print("File_in provided from cmd")
finally:# εαν δεν φορτωνει ο χρηστεις ελεγχη εαν υπαρχει αρχειο στο φακελο
    if os.path.isfile(file_in):
        print("File is successfully detected")
    else:# εαν δεν υπαρχει αρχειο στο φακελο τερματιζει
        print("Could not detect sampletext, terminating.")
        sys.exit(2)

x=open("sampletext.txt","r",encoding="utf-8")# ανοιγει το αρχειο

text_ascii=parse_file()# καλω την συναρτηση

value=[]
 
for i in text_ascii:#δημιουργω μια λιστα απο λεξεις στην οποια δεν υπαρχει ο κενος χαρακτηρας
    if i!='':
        value.append(i)


for i in range(0,len(value)):# κανω λιστα καθε λεξει που υπαρχει στην λιστα value
    value[i]=[char for char in value[i] ]

single=[]
for i in range(0,len(value)):
    for j in range(0,len(value[i])):
        if ord(value[i][j])<129:#ελεγχω εαν ο καθε χαρακτηρας στην value ειναι μικροτερος του 129
            if ord(value[i][j])%2 == 1: # αν ειναι μονος τον κανω append στην single
                single.append(ord(value[i][j]))
        else:
            print("this char",value[i][j],"not exist")

percent = []
for element in single:
    if [element,single.count(element)*100/len(single)] not in percent:# ελεγχω εαν υπαρχει το νουμερο μαζι με το ποσες φορες εμφανιζεται
        percent.append([element,single.count(element)*100/len(single)])# εαν δεν υπαρχει το κανω append στην precent μαζι με τον αριθμο των εμφανισεων του
    
for element in percent:
    print(element[0],round(element[1]+0.5)*"*")# κανω print τον αριθμο μαζι με τις εμφανισεις του τις οποιες τις στρογγυλοποιο προς τα πανο 