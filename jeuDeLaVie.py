from random import *
from tkinter import *

def Plateau(x):
    global plateau,plateaucopie
    plateau = [[0]*x for loop in range(x)] 
    plateaucopie = [[0]*x for k in range(x)] #Le plateau pour faire les calculs
                    
def ConditionInitial(cellules): #Pour déterminer quelles cellules vont être vivantes au départ (aléatoirement)
    for loop in range(cellules):
        coordx,coordy = int(randint(0,nbCases)),int(randint(0,nbCases))
        plateau[coordx%nbCases][coordy%nbCases] = 1
    


def test(): #Pour calculer quelles cellules vont être vivantes ou mortes au prochain tour (1=vivante, 0=morte)
    global plateau,plateaucopie
    for ligne in range(nbCases):
        for colonne in range(nbCases):
            somme = 0
            for testligne in range(ligne-1,ligne+2):
                for testcolonne in range(colonne-1,colonne+2):
                    somme += plateau[testligne%nbCases][testcolonne%nbCases] #On fait la somme de toutes les valeur autour de la cellule
            somme -= plateau[ligne][colonne] #On enlève au total la valeur de la cellule regardée
            if plateau[ligne][colonne] == 1: #Si la cellule est vivante
                if somme != 2 and somme != 3:
                    plateaucopie[ligne][colonne] = 0
                else:
                    plateaucopie[ligne][colonne] = 1
            else: #Si la cellule est morte
                if somme == 3:
                    plateaucopie[ligne][colonne] = 1
    for n in range(nbCases):
        for n2 in range(nbCases):
            plateau[n][n2] = plateaucopie[n][n2]

def calculerTableau(): #Pour changer ce qui est affiché (noir = vivant, blanc = mort)
    
    for ligne in range(nbCases):
        for colonne in range(nbCases):
            if plateau[ligne][colonne]==0:
                canvas.create_rectangle(ligne*tailleCellules,colonne*tailleCellules,(ligne+1)*tailleCellules,(colonne+1)*tailleCellules,fill = "white")
            else:
                    
                canvas.create_rectangle(ligne*tailleCellules,colonne*tailleCellules,(ligne+1)*tailleCellules,(colonne+1)*tailleCellules,fill = "black")    
    
def iteration():    #On appelle cette fonction à chaque itération
    test()
    calculerTableau()

                

nbCases = int(input("Nombre de cellules par lignes: "))
tailleCellules = 25 #Pour changer la taille des cellules (en pixel)
nbCellulesActivesInit = int(input("Cellules actives au départ: "))
Plateau(nbCases)
ConditionInitial(nbCellulesActivesInit)


master = Tk()
master.title("Jeu de la vie")
canvas = Canvas(master,width=nbCases*tailleCellules,height=nbCases*tailleCellules)
canvas.grid(row=1,column=1,columnspan=2)

buttonIteration = Button(master,text="Prochaine étape", command = iteration)
buttonIteration.grid(row=2,column=1)

buttonQuit = Button(master,text="Quitter",command = master.destroy)
buttonQuit.grid(row=2,column=2)

calculerTableau()

master.mainloop()
        
