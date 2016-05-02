# Créé par Maxime, le 11/03/2016 en Python 3.2
def etoile (motachercher):
    resultat = motachercher[0]
    for i in range (len(motachercher)-1):
        resultat = resultat + "*"
    return resultat
mot = input ("veuillez saisir le mot")
mot1 = etoile(mot)
print (mot1)

