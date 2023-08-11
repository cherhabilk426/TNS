# Programmes pris de openclassroom
#https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python


##Les objets :chaines, listes, etc.
import os
##os.system('cls')
########### Les chaines
##chaine="BONJOUR les FUTUR(E)S DIPLOME(E)S"
##print(chaine.lower())
##print(chaine.capitalize())
##chaine[3]='s';chaine[4]='o';chaine[5]='i'  ca ne marche pas
##chaine="Bonsoir"+chaine[7:]
##print(chaine)


########### Les listes
##ma_liste = ['a', 'b', 'd', 'e']
##ma_liste.insert(2, 'c') 
##print(ma_liste)
##del ma_liste[0]  
##print(ma_liste)
##ma_liste.remove('d')
##print(ma_liste)
##ma_liste[0]="Bonjour"
##print(ma_liste)
##ma_liste.append(2019)
##print(ma_liste)

##ma_liste1 = [3, 4, 5]
##ma_liste2 = [8, 9, 10]
##ma_liste1.extend(ma_liste2) 
##print(ma_liste1)
##
##ma_liste3 = [1, 2, 6, 7]
##ma_liste1 += ma_liste3 
##print(ma_liste1)


######### Les tuples
##ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
##for i in enumerate(ma_liste):
##    print(i)
##
##
##for i, j in enumerate(ma_liste):
##     print("A l'indice %d se trouve %s."%(i, j))
##
##liste_origine = [0, 1, 2, 3, 4, 5]
##print([nb * nb for nb in liste_origine])

######### Les fichiers
##fichier = open("fichier.txt", "w") 
##fichier.write("Premier test d'écriture dans un fichier via Python")
##fichier.close()
##fichier = open("fichier.txt", "r")
##contenu=fichier.read()
##print(contenu)
##fichier.close()
##
##file = open("fichier.txt", 'w') 
##file.write('hello world !') 
##file.close() 
##  
##file = open("fichier.txt", 'w') 
##try: 
##    file.write('hello world') 
##finally: 
##    file.close() 
## 
##with open("fichier.txt", 'w') as file: 
##    file.write('hello world !')

