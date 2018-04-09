# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from numpy import ndindex, ndenumerate
from numpy import random
from tkinter import*
from tkinter import ttk
import time
import random


puzzle = [[8,0,0,0,0,0,0,0,0],
          [0,0,3,6,0,0,0,0,0],
          [0,7,0,0,9,0,2,0,0],
          [0,5,0,0,0,7,0,0,0],
          [0,0,0,0,4,5,7,0,0],
          [0,0,0,1,0,0,0,3,0],
          [0,0,1,0,0,0,0,6,8],
          [0,0,8,5,0,0,0,1,0],
          [0,9,0,0,0,0,4,0,0]]

        
    
        
puzzle = np.array(puzzle)

root=Tk()
root.configure(background='black')
 
# hey saluuuut

var=[]
for i in puzzle:
    for x in i:
        if x == 0:
            x = ""
        y=StringVar()
        y.set(x)
        var.append(y)
        
    
var= np.array(var)




count = 0
for i in range(9):
    for j in range(9):   
        if puzzle[i,j] == 0:
            Label(root, textvariable=var[count],width=4, height=2, font=("Arial", 16),foreground="black", background="#D9949F").grid(row=i, column=j, padx = 1, pady =1)
        else:
            Label(root, textvariable=var[count],width=4, height=2, font=("Arial", 16),foreground="black").grid(row=i, column=j, padx = 1, pady =1)

        
        count += 1
        
        
        
        
        

var = var.reshape(9,9)


def bonchiffre(chiffre, row, column):
    x = box(row, column)
    if chiffre in puzzle[row] or chiffre in puzzle[:, column] or chiffre in puzzle[x[0]:x[1], x[2]:x[3]]:
        return False
    return True


def box(row, column):
    uprow = [(row + i) for i in range(1, 4) if (row + i) % 3 == 0][0]
    downrow = uprow - 3
    upcolumn = [(column + i) for i in range(1, 4) if (column + i) % 3 == 0][0]
    downcolumn = upcolumn - 3
    return [downrow, uprow, downcolumn, upcolumn]

def SolveSudoku(puzzle):


    z=[(index, x) for index, x in np.ndenumerate(puzzle)]
    z = np.array(z)
    inconnues = z[z[:,1]==0]  # indexes des cases qu'on peut modifier*$


    i=0   
    counter = 0
    
    while i <= len(inconnues):        
        
        if i == (len(inconnues)):  
            print(counter)
            return puzzle
            break
        
            
        for j in range((puzzle[inconnues[i][0][0],inconnues[i][0][1]]),10):
            
            if bonchiffre(j, inconnues[i][0][0], inconnues[i][0][1]) == True  :
                puzzle[inconnues[i][0][0], inconnues[i][0][1]] = j 
                var[inconnues[i][0][0], inconnues[i][0][1]].set(j)
                root.update()
                # time.sleep(.02)


                counter += 1                
                i += 1                
                break
          

            if bonchiffre(j, inconnues[i][0][0], inconnues[i][0][1]) == False and j==9 :
                puzzle[inconnues[i][0][0], inconnues[i][0][1]] = 0   
                var[inconnues[i][0][0], inconnues[i][0][1]].set("")
                
                root.update()
                # time.sleep(.02)
                counter += 1
                i -= 1                        
                break


SolveSudoku(puzzle)
root.update()
root.mainloop()


