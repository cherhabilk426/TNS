# Programmes pris de
# openclassroom https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python

# -*- coding: utf8 -*-
######
def table_par_7():
    nb = 7;   i = 0 
    while i < 10:
        print('%d * %d = %d '%(i + 1, nb, (i + 1) * nb))
        i += 1

table_par_7()

######
def table(nb,max=10):
    i = 0 
    while i < max:
        print('%d * %d = %d '%(i + 1, nb, (i + 1) * nb))
        i += 1

table(8)
table(8,11)


######
def fonction_inconnue(*parametres):
    print("J'ai re�u : {}.".format(parametres))

fonction_inconnue() 
fonction_inconnue(33)
fonction_inconnue('a', 'e', 'f')
var = 3.5
fonction_inconnue(var, [4], "...")


######       
def carre(valeur):
    return valeur * valeur

print(carre(5))

######
f = lambda x: x * x
print(f(5))

######
import math
print(math.sqrt(16))

import math as mathematiques
print(mathematiques.sqrt(16))

from math import sqrt  
print(math.sqrt(16))

import os # On importe le module os qui dispose de variables  et de fonctions utiles pour dialoguer avec le syst�me d'exploitation


####### Try except
##a,b=5,0
##try:
##   x = a / b
##except NameError:
##    print("La variable numerateur ou denominateur n'a pas �t� d�finie.")
##except TypeError:
##    print("La variable numerateur ou denominateur poss�de un type incompatible avec la division.")
##except ZeroDivisionError:
##    print("La variable denominateur est �gale � 0.")
##else:
##    print("Le r�sultat obtenu est", x)

##annee = input("Saisissez une ann�e sup�rieure � 0 :")
##try:
##    annee = int(annee) # Conversion de l'ann�e
##    assert annee > 0
##except ValueError:
##    print("Vous n'avez pas saisi un nombre.")
##except AssertionError:
##    print("L'ann�e saisie est inf�rieure ou �gale � 0.")    
###os.system("pause")
