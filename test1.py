# Créé par Alexis, le 08/12/2015 en Python 3.2

from lycee import*
total =0
prix_max = 0
for i in range (1,4,1):
    prix_unit = demande("Prix unitaire")
    if prix_max < prix_unit:
        prix_max = prix_unit
    nb_art = demande("Nombre d'articles")
    prix_tot = prix_unit*nb_art
    print("Vous devez payer : ",prix_tot)
    total = total + prix_tot

print("le prix total à payer est de ",total," €")
print("le montant le plus élevé est de ",prix_max," €")
