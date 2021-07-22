'''
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.
Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και γεμίζει στην τύχη τις μισές με S και τις μισές με O (στρογγυλοποίηση προς τα πάνω). 
Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια, κάθετα, και διαγώνια. 
Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο όρο των τριάδων SOS.

'''
"""
Όνομα: Ηρακλής 
Επώνυμο: Τσίκας
ΑΜ : ΜΠΠΛ20082
"""
import random
# ζητάμε απο τον χρήστει να δώσει τις 2 πλευρές
x=(int(input("Δώσε την οριζόντια πλευρά του ορθογωνίου: ")))
y=(int(input("Δώσε την κάθετη πλευρά του ορθογωνίου: ")))
sum=0
# για να κανουμε επαναληψη 100 φορες το βαζουμε σε λουπα
for i in range(0,100):
    print("Γύρος: ",i+1)
    S=0# για να μετραει τα S ποσα εχουν μπει
    O=0# για να μετραει τα Ο ποσα εχουν μπει
    sos_table=[]
    values=round(x*y/2)
    #βρισκω με στρογγυλοποιηση προς τα κατω τα Ο στοιχεια που θα εχει ο πινακας μου
    #τα S εχω αποφασισει οτι θα εχουν παραπανω θεσει στον πινακα απο τα Ο για αυτο και στην loop βαζω x*y-values
    #γεμίζουμε τον πινακα του παιχνιδιου 
    for i in range(0,x):
        temp=[]
        for j in range(0,y):
            if S<(x*y-values) and O<values: 
                # αν ισχυουν και οι 2 παραμετροι γεμιζει μια μεταβλητη value τυχαια και κανει ελεγχο και τα προσθετει στην temp
                value=random.choice(["S","O"])
                if value == "S":
                    S=S+1
                else:
                    O=O+1
                temp.append(value)
            elif S == (x*y-values):# αν ο μετρητης S ειναι ισο με x*y-values το τοτε κανει append O
                temp.append("O")
                O=O+1
            else:
                temp.append("S")
                S=S+1
        sos_table.append(temp)

    #print("S:{0},O:{1}".format(str(S),str(O)))
    
    for i in range(0,x):
        for j in range(0,y):
            print(sos_table[i][j],end=" ")
            # λεω στην print  να μην παει στην απο κατω γραμμη οπως θα κανει απο μονη της και οσο μενει στην for j
            # να μου  τυπωνει τα στοιχεια το ενα διπλα στο αλλο
        print(" ")
        # με το που τελειωσει στην for j κανω print για να παει στην επομενη γραμμη και να μοιαζει στο τελος με παιχνιδι sos

    #βρισκουμε τα οριζοντια ΣΟΣ
    horizontal=0
    for i in range(0,x):
        for j in range(0,y):
            if j<y-2: # βαζω το j να σταματαει 2 θεσεις πριν το y γιατι το SOS εχει μηκος 3=αυτο που υπολογιζει+ τα 2 επομενα οποτε να μην βγαλει error οταν δεν εχει αλλα μετα απο το y
                if sos_table[i][j]=="S":
                    if sos_table[i][j+1]=="O":
                        if sos_table[i][j+2]=="S":
                            horizontal=horizontal+1
    print("Οριζόντια",horizontal)

    #βρισκουμε τα καθετα ΣΟΣ
    vertical=0
    for i in range(0,y):
        for j in range(0,x):
            if i<x-2:# βαζω το ι να σταματαει 2 θεσεις πριν το χ γιατι το SOS εχει μηκος 3=αυτο που υπολογιζει+ τα 2 επομενα οποτε να μην βγαλει error οταν δεν εχει αλλα μετα απο το χ
                if sos_table[i][j]=="S":
                    if sos_table[i+1][j]=="O":
                        if sos_table[i+2][j]=="S":
                            vertical=vertical+1
    print("Κάθετα",vertical)

    #βρισκουμε τα διαγωνια ΣΟΣ
    diagonal=0
    for i in range(0,x):
        for j in range(0,y):
            if i<x-2 and j<y-2:# για να μην μου κοιταζει εκτος πινακα και γυρναει error
                if sos_table[i][j]=="S":
                    if sos_table[i+1][j-1]=="O":
                        if sos_table[i+2][j-2]=="S":
                            diagonal=diagonal+1
    print("Διαγώνια",diagonal)

    #βρισκουμε τα διαγωνια ΣΟΣ απο την αντιθετη μεριά του πινακα
    reverse_diagonal=0
    for i in range(0,x):
        for j in range(0,y):
            if i<x-2 and j>=2:
            # βαζω το ι να σταματαει 2 θεσεις πριν το χ γιατι το SOS εχει μηκος 3=αυτο που υπολογιζει+ τα 2 επομενα οποτε να μην βγαλει error οταν δεν εχει αλλα μετα απο το χ
            # και βαζω j>=2 για να αρχισει μετραει απο την 3 θεσει και ναμπορεσουν τα εμφολευμενα if να μου μετραει αντιστροφα και να μην μου γυρισει error
                if sos_table[i][j]=="S":
                    if sos_table[i+1][j-1]=="O":
                        if sos_table[i+2][j-2]=="S":
                            reverse_diagonal=reverse_diagonal+1
    print("Αντίθετα διαγώνια",reverse_diagonal)
    
    
    total_round=horizontal+vertical+diagonal+reverse_diagonal
    sum=sum+total_round
    print("Total",total_round)
    print("")
average=sum/100
print("Μεσος ορος",average)
