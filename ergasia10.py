"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου
και μετατρέπει τον κάθε χαρακτήρα του στον “κατοπτρικό” του χαρακτήρα ASCII. 
Κατοπτρικοί χαρακτήρες είναι αυτοί των οποίων το άθροισμα είναι 128.
Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.
"""
"""
Όνομα: Ηρακλής 
Επώνυμο: Τσίκας
ΑΜ : ΜΠΠΛ20082
"""
import sys
import os
import re


def parse_file():
    
    text=x.read()
    text=re.sub('[^A-Za-z0-9 ]+', '', text)#αντικαθιστω με κενα οπου υπαρχει [, . !? "" () και την αλλαγη γραμμης]
    text_ascii = text.split(" ")# οπου υπαρχει κενο κανω split
    return (text_ascii)

try:# ελεγχη εαν ο χρηστεις φορτωνει αρχειο
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
#δημιουργω μια λιστα απο λεξεις στην οποια δεν υπαρχει ο κενος χαρακτηρας 
for i in text_ascii:
    if i!='':
        value.append(i)

# κανω λιστα καθε λεξει που υπαρχει στην λιστα value
for i in range(0,len(value)):
    value[i]=[char for char in value[i] ]




        
# βρισκω τον κατοπτρικο χαρακτηρα σε καθε χαρακτηρα στην value και τον αντικαθιστω
for i in range(0,len(value)):
    for j in range(0,len(value[i])):
        if ord(value[i][j])<129:

            value[i][j]=chr(128-ord(value[i][j]))# βρισκω τον κατοπτρικο χαρακτηρα σε καθε χαρακτηρα του value και τον αντικαθιστω
        else:
            print("Char",value[i][j],"is not ASCII")

# αναποδογυριζω την λιστα value
value.reverse()

#και συνδεω τα γραμματα για να φτιαξω λεξεις και στην συνεχεια τισ λεξεις  για να φτιαξω το κειμενο
for i in range(0,len(value)):
    value[i]="".join(value[i])
value=" ".join(value)


print(value)