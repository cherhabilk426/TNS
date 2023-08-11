
# Certaines parties sont prises de 
# openclassroom https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python

### Fonction input et print
print("Bonjour le monde !")
A = "TPs"
B = "Chargée"
C = "TSA"
print("Je suis {0} des {1} du module {2} ce semestre.".format(B, A, C))
print("Je suis %s des %s du module %s ce semestre." % (B, A, C))

# a,b= input("Donner deux nombres : ").split()
# print("a=%s b =%s"%(a,b))
# a=int(a);b=int(b)
# c=a+b
# print("c=%d"%(c))

# ####### Affectation
# a,b = b,a
# print('Après permutation, la valeur de a est %s et b est %s'%(a,b))


##### Structure "if else elif" et Opérateurs logiques
# a=input("Donnez une valeur "); a=int(a)
# if a >= 0:
#     if a <= 20:
#         print("C'est une note")  
#         print("oui je sais")
#     else:
#         print("Ce n'est pas une note")
# else:
#     print("Ce n'est pas une note !!")
    
    
# x = 10; y = 12; z=14
# print("x > y  is " +str("Bonjour"))
# print('x <= y  is %s' %(x<= y))

# if x > y:
#     print("%d est plus grand que %d"%(x,y))
           
# else:
#     if x == y:
#         print("Ils sont égaux")
  
# if x < y < z:
#     print(x); print(y); print(z)
# ####
# annee = input("Saisissez une année: ")
# annee = int(annee) 

# if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
#     print("L'année saisie est bissextile.")
# else:
#     print("L'année saisie n'est pas bissextile.")


# ##### Les boucles
# nb = 7; i = 1

# while i <= 10: 
#     print( "%d * %d = %d" %(i,nb, i * nb) )
#     i+=1

# maliste=[16,32,48]
# for k in maliste :
#   print(2*k)

# for i in range(11) :
#     print ( "Et %d ! "%(i))
  
# chaine = "Bonjour Télécom"
# for i in chaine:
#  print(i)

# j=0
# for lettre in chaine:
#   if lettre in "AEIOUYaeiouyéè":
#         print(lettre);
#         j=j+1;

# # ##
# print("Le nombre de voyelles est % d"%j)#Enlever le saut de ligne et observer
    
# while 1: 
#     lettre = input("Tapez 'Q' pour quitter : ")
#     if lettre=='Q':
#         print("Fin de la boucle")
#         break

# i = 1
# while i < 20: 
#     if i % 3 == 0:
#         i += 4 
#         print("On incrémente i de 4. i est maintenant égale %d "%i)
#         continue 
#     print("La variable i = % d " % i)
#     i += 1 
 
###### Les fonctions
# def table_par_7():
#     nb = 7;   i = 0 
#     while i < 10:
#         print('%d * %d = %d '%(i + 1, nb, (i + 1) * nb))
#         i += 1

# table_par_7()

# ##
# def table(nb,max=10):
#     i = 0 
#     while i < max:
#         print('%d * %d = %d '%(i + 1, nb, (i + 1) * nb))
#         i += 1

# # table(7)
# # table(8)
# table(8,11)

# ##
# def fonction_inconnue(*parametres):
#     print("J'ai reçu : {}".format(parametres))

# fonction_inconnue() 
# fonction_inconnue(33)
# fonction_inconnue('a', 'e', 'f')
# var = 3.5
# fonction_inconnue(var, [4], "...")

# ###      
# def carre(valeur):
#     a=valeur*valeur
#     print("le carré de %d est %d"%(valeur,a))
#     return a, a*a

# b,c=carre(-3)
# print(b,c)

# ######
# f = lambda x: x * x * x
# print(f(5))

# # ######
# import math
# a=math.sqrt(16)
# print(a)

# import math as mt
# a=mt.sqrt(16)
# print(a)

# from math import sqrt  
# a=sqrt(16)
# print(a)

# ######### Les listes et tableaux
#pas de délaration, séquence courte
# A = ['nom','prénom','SG',6, [1,3,-7]]
# print(A)
# print(A[1]); 
# N=len(A); print(N)
# A.append("Master: RT")    #Tester insere remove
# print(A)

# déclaration, se prète mieux aux opérations numériques
import numpy as np
# B = np.array(['nom','prénom','SG',6])
# print(B)
# print(B[-3]); 
# print(B[:2]);
# print(B[2:]);
# C=B[::-1]; print(C)

# A=np.array([2,5,-7, 7, 2]); 
# B=A
# print(A, B)
# B[0]=9
# print(A, B)

# from copy import deepcopy
# A=np.array([2,5,-7]); 
# B=deepcopy(A)
# print(A, B)
# B[0]=9
# print(A,B)

#n=2 ; m=3;
# # C = [[0]*m for i in range(n)]; print (C)
# # C = np.zeros((n,m)); print(C)
#C = np.array([[1, 2, 3], [4, 5, 6]]); print (C)
# print(C[0]); print(C[1]); print(C[0,2])
# n=len(C) # nombre de lignes
# m=len(C[0]) # nombre de colonnes
 
# A=np.zeros((m,n));
#print(A)
# parcourir les lignes
# for i in range(n):
#     # parcourir les colonnes
#     for j in range(m):
#         A[j][i]= C[i][j]
# print(A)

# B = [[C[j][i] for j in range(n)] for i in range(m)]
# print(B)

#D=C.reshape(3,2); print (D)

# ######### Les fichiers
# fichier = open("fichier.txt", "w") 
# fichier.write("Premier test d'écriture dans un fichier via Python")
# fichier.close()

# fichier = open("fichier.txt", "r")
# contenu=fichier.read()
# print(contenu)
# fichier.close()

# file = open("fichier.txt", 'w') 
# file.write('hello world !') 
# file.close() 


  
# file = open("fichier.txt", 'w') 
# try: 
#     file.write('hello world') 
# finally: 
#     file.close() 

# with open("fichier.txt", 'w') as file: 
#     file.write('hello world !')









