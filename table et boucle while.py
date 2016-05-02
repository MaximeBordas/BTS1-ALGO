# Créé par Alexis, le 15/12/2015 en Python 3.2
from lycee import *
jours =[" Lundi","Mardi"," Mercredi","Jeudi" ," Vendredi"," Samedi" ," Dimanche"]
mois=["Janvier" ,"Février","Mars","Avril","Mai","Juin","Juillet","Août"]
mois=mois+["Septembre","Octobre","Novembre","Décembre"]
nbjours=[31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]

ind = 0
while ind < 12:
    print ("Le mois de",mois[ind]," possède",nbjours[ind], "jours")
    ind = ind + 1

