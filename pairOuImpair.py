# Créé par Maxime, le 18/04/2016 en Python 3.2
from lycee import *
def estPair(nbr1):
    if (nbr1 % 2 == 0):
        return True
    else:
        return False
nombre1 = int(input("veillez saisir un nombre"))
resultat = estPair(nombre1)
if(resultat == True) :
    print ("Le nombre est pair")
else :
    print("Le nombre est impair")
