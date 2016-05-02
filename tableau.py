# Créé par Maxime, le 02/02/2016 en Python 3.2
from lycee import *
tab = [1,25,13,26,45]
choix = demande("Veuillez choisir un nombre")
trouve= False
for i in range(0,len(tab),1):
    if tab[i]==choix:
        trouve = True
if trouve==True:
    print("La valeur existe dans le tableau")
else:
    print("La valeur n'existe pas dans le tableau")
total=0


for i in range(0,len(tab),1):
    total= tab[i]+total

print(total/len(tab))

for i in range (0,len(tab),1):
    max=tab[0]
    if max < tab[i]:
        max= tab[i]
print("La valeur max est ",max)

for i in range (0,len(tab),1):
    min=tab[0]
    if min > tab[i]:
        min= tab[i]
print("La valeur min est ",min)

total= total-min-max
print("La nouvelle moyenne est",total/(len(tab)-2))