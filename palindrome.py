# Créé par Maxime, le 11/03/2016 en Python 3.2
def palindrome(chaine):
    i, longueur = 0, len(chaine)

    while i < longueur:
        if chaine[i] != chaine[-i - 1]:
              return False
        i += 1

    return True

if palindrome(input("saisissez le mot")):
    print ("Palindrome.")
else:
    print ("Pas palindrome.")