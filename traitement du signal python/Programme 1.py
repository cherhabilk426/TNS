
# Programmes pris de 
# openclassroom https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python

### Fonction input
##print("Bonjour le monde !")
##print('Bonjour {Nom}, {Question}'.format(Question= 'Ca va?', Nom = 'Sections A ou B'))
####A=2; 
prenom = "abdelkarim"
nom = "cherhabil"
age = "26"
print("Je m'appelle {1} {0} et j'ai {2} ans.".format(prenom, nom, age))
print("Je m'appelle % s %s et j'ai %s ans." % (prenom, nom, age))
####
####
####
####### Fonction input
##a,b= input("Donner deux nombres : ")
####
####
####
####### Affectation
##a,b = b,a
##print('Apr�s permutation, la valeur de a est {} et b est {}'.format(a,b))
##
##
##
##
##### Structure "if else elif" et Op�rateurs logiques
##if a >= 0:
##    if a <= 20:
##        print("C'est une note")
##        
##    else:
##        print("Ce n'est pas une note")
##else:
##    print("Ce n'est pas une note")

##x = 10; y = 12; z=14
##print("x > y  is" +str(x>y))
##print('x <= y  is {}'.format(x<= y))
##if x > y:
##  print("x est plus grand que y")
##elif x == y:               #Regarder elif pour else if
##  print("Ils sont �gaux")
##  
##if x < y < z: print(x); print(y); print(z)
####
##annee = input("Saisissez une ann�e: ")
##annee = int(annee) 
##bissextile = False 
##
##if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
##    print("L'ann�e saisie est bissextile.")
##else:
##    print("L'ann�e saisie n'est pas bissextile.")

##
##
##### Les boucles
nb = 7; i = 0 

while i < 10: 
    print( "%d*%d=%d"%(i+1,nb, (i + 1) * nb))
    i += 1 

maliste=[2,3,4]
for k in maliste :
  print(2*k)

for i in range(1,4) :
    print ( "Et %d ! "%i)
  
chaine = "Bonjour T�l�com"
for i in chaine:
    print(i)

j=0
for lettre in chaine:
    if lettre in "AEIOUYaeiouy": 
        print(lettre);
        j+=1

##
print("Le nombre de voyelles est % d"%j)#Enlever le saut de ligne et observer
    
while 1: 
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre=='Q':
        print("Fin de la boucle")
        break

i = 1
while i < 20: 
    if i % 3 == 0:
        i += 4 
        print("On incr�mente i de 4. i est maintenant �gale {}�". format(i))
        continue 
    print("La variable i = % d " % i)
    i += 1 









