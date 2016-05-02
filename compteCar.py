# Créé par Maxime, le 02/05/2016 en Python 3.2
from lycee import *
def compteCar(ca,ch) :
    count = 0
    for ind in range (len(ch)):
        if (ca.lower() == ch[ind].lower()) :
            count = count + 1
    return count

print(compteCar("S","Salutations"))
