"""
Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι.
Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a να ισχύει ότι a^p=a mod p. 
Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.
"""
"""
Όνομα: Ηρακλής 
Επώνυμο: Τσίκας
ΑΜ : ΜΠΠΛ20082
"""
import random
import os 
import sys

#συναρτηση με την οποια βρισκο τον αριθμο fibonacci
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # Αν ο αριθμος που εδωσε ο χρηστεις ειναι 1 τοτε επιστρεφει 0 γιατι ο αριθμος fibonacci του 1 ειναι 0
    elif n==1: 
        return 0
    # Αν ο αριθμος που εδωσε ο χρηστεις ειναι 2 τοτε επιστρεφει 1 γιατι ο αριθμος fibonacci του 2 ειναι 1 
    elif n==2: 
        return 1
    else: #εαν ο αριθμος ειναι μεγαλυτερος απο 2 κανει αναδρομη
        return Fibonacci(n-1)+Fibonacci(n-2)

x=(int(input("Enter a number:")))
fib_num=(Fibonacci(x)) #καλο την συναρτηση για να βρω τον αριθμο fibonacci 
print("Fibonacci number of {0} is: {1} ".format(x,fib_num))

z=[]
# φτιαχνω μια λιστα που θα την γεμισω με του τυχαιου αριθμου απο το 1 εως τον αριθμο fibonacci 
# για να κάνω τον ελεγχο στην συνεχεια
for i in range (0,20):
    z.append(random.choice(range(1,fib_num)))
    #με random.choice γεμιζω την λιστα z με τυχαιους αριθμους απο το 1 εως fib_num χωρις το 0
print("The list with random numbers is: {0}".format(z))

print("Fibonacci number: {0} ".format(fib_num))

for item in z:
    check = (item ** fib_num) - item
    if check % fib_num == 0:
        # εαν το υπολοιπο ειναι 0 συνεχιζει με τους υπολοιπους αριθμους στην λιστα z
        continue
    else:
        # αν εχει υπολοιπο  ειναι 0 τοτε τυπωνει οτι δεν ειναι πρωτος και βγαινει τελειως απο την for loop
        print("Its not a prime number")
        sys.exit(2)
    
print("The number is a prime")




























