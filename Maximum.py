# Créé par Maxime, le 26/04/2016 en Python 3.2
from lycee import *

def maximum(nbr1, nbr2, nbr3):
    if (nbr1 >nbr2 and nbr1 > nbr3):
        resultat = nbr1
        return resultat
    else:
        if(nbr2>nbr3):
            resultat = nbr2
            return resultat
        else:
            resultat = nbr3
            return resultat

print(maximum(3,3,3))


