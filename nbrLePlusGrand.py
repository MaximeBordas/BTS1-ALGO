# Créé par Maxime, le 18/04/2016 en Python 3.2
from lycee import *
def nbrLePlusGrand (nbr1,nbr2) :
    if (nbr1<nbr2) :
        return nbr2
    else :
        return nbr1
nombre1 = input("Veuillez saisir le nombre n°1")
nombre2 = input("Veuillez saisir le nombre n°2")
resultat = nbrLePlusGrand(nombre1, nombre2)
print(resultat)

