# Créé par Maxime, le 01/04/2016 en Python 3.2
from lycee import *

word=input()
seq=input()
tabSeq=[]
word=word.lower()
seq=seq.lower()

#ON met les lettres de la séquence dans une liste pour utiliser remove() plus tard

for lettres in seq:
    tabSeq.append(lettres)

#On parcours toutes les lettres du mot
for lettreInMot in word:
    ind=0
    trouve=False
    while trouve==False and ind<len(tabSeq):
        if lettreInMot==tabSeq[ind]:
            trouve = True
            tabSeq.remove(lettreInMot)
        else:
            ind=ind+1
if ind==len(tabSeq):
    print("Le mot est impossible a crée avec cette séquence!")
elif trouve==True:
    print("Le mot est présent dans la séquence !")
