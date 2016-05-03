# Créé par Maxime, le 04/02/2016 en Python 3.2
from tkinter import *
for i in range (0,100,1):
    fenetre = Tk()

    fenetre.geometry("200x250")
    fenetre.title("Swaglord")
    quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)



    fenetre.mainloop()