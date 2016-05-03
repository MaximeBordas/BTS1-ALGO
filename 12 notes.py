# Créé par Maxime, le 12/01/2016 avec EduPython
from lycee import *


for i in range (0,12,1):
    note.append(randint(0,20))
    print(note[i])
noteChoisie = demande("Veuillez saisir une note")
noteDansTableau = false
i=0
while noteDansTableau == false or i>=12:
    if noteChoisie == note[i]:
        noteDansTableau = true
    i = i+1

if noteDansTableau == false:
    print("La valeur saisie n'est pas dans le tableau")
else:
    print("La valeur saisie est dans le tableau !")