import numpy as np
from tkinter import *

puzzle = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 3, 6, 0, 0, 0, 0, 0],
          [0, 7, 0, 0, 9, 0, 2, 0, 0],
          [0, 5, 0, 0, 0, 7, 0, 0, 0],
          [0, 0, 0, 0, 4, 5, 7, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 3, 0],
          [0, 0, 1, 0, 0, 0, 0, 6, 8],
          [0, 0, 8, 5, 0, 0, 0, 1, 0],
          [0, 9, 0, 0, 0, 0, 4, 0, 0]]

puzzle = np.array(puzzle)
root = Tk()
root.configure(background='black')
var = []

# Creation du tableau des variables
for i in puzzle:
    for x in i:
        if x == 0:
            x = ""
        y = StringVar()
        y.set(x)
        var.append(y)

var = np.array(var)
count = 0

# Rendu de la grille initiale contenant le tableau des variables
for i in range(9):
    for j in range(9):
        if puzzle[i, j] == 0:
            Label(root, textvariable=var[count], width=4, height=2, font=("Arial", 16), foreground="black",
                  background="#D9949F").grid(row=i, column=j, padx=1, pady=1)
        else:
            Label(root, textvariable=var[count], width=4, height=2, font=("Arial", 16), foreground="black").grid(row=i,
                                                                                                                 column=j,
                                                                                                                 padx=1,
                                                                                                                 pady=1)
        count += 1
        
var = var.reshape(9, 9)


def bonchiffre(chiffre, row, column):
    bonchiffrex = box(row, column)
    if chiffre in puzzle[row] or chiffre in puzzle[:, column] or chiffre in puzzle[bonchiffrex[0]:bonchiffrex[1],
                                                                                   bonchiffrex[2]:bonchiffrex[3]]:
        return False
    return True


def box(row, column):
    uprow = [(row + boxi) for boxi in range(1, 4) if (row + boxi) % 3 == 0][0]
    downrow = uprow - 3
    upcolumn = [(column + boxi) for boxi in range(1, 4) if (column + boxi) % 3 == 0][0]
    downcolumn = upcolumn - 3
    return [downrow, uprow, downcolumn, upcolumn]


def solvesudoku(gridsudo):
    z = [(index, solvex) for index, solvex in np.ndenumerate(gridsudo)]
    z = np.array(z)
    inconnues = z[z[:, 1] == 0]  # indexes des cases qu'on peut modifier
    solvei = 0

    while solvei <= len(inconnues):
        if solvei == (len(inconnues)):
            return gridsudo
        for J in range((gridsudo[inconnues[solvei][0][0], inconnues[solvei][0][1]]), 10):

            if bonchiffre(J, inconnues[solvei][0][0], inconnues[solvei][0][1]):
                gridsudo[inconnues[solvei][0][0], inconnues[solvei][0][1]] = J
                var[inconnues[solvei][0][0], inconnues[solvei][0][1]].set(J)
                root.update()
                solvei += 1
                break

            if not bonchiffre(J, inconnues[solvei][0][0], inconnues[solvei][0][1]) and J == 9:
                gridsudo[inconnues[solvei][0][0], inconnues[solvei][0][1]] = 0
                var[inconnues[solvei][0][0], inconnues[solvei][0][1]].set("")
                root.update()
                solvei -= 1
                break


solvesudoku(puzzle)
root.update()
root.mainloop()