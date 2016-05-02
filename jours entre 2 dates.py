# Créé par Alexis, le 15/12/2015 en Python 3.2
# Créé par Alexis, le 15/12/2015 en Python 3.2
from lycee import *
jours =[" Lundi","Mardi"," Mercredi","Jeudi" ," Vendredi"," Samedi" ," Dimanche"]
mois=["Janvier" ,"Février","Mars","Avril","Mai","Juin","Juillet","Août"]
mois=mois+["Septembre","Octobre","Novembre","Décembre"]
nbjours=[31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]

numJour = demande("Veuillez saisir le jour (en nombre)")
numMois = demande("Veuillez saisir le mois (en nombre)")
ind = numMois
jourTotal =0
while ind > 0:
    ind = ind -1
    jourTotal = jourTotal + nbjours[ind]
