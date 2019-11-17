# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:49:54 2019

@author: primp
"""

def aminciLdeux(Image):
    s = Image.shape
    resultat = Image.copy()
    for ligne in range(1,s[0]-2):
        for colonne in range(1,s[1]-2):
            #ligne du haut :voisins
            if (Image[ligne-1,colonne-1]==1) and (Image[ligne-1,colonne+1]==0) :
                #ligne du bas
                if  (Image[ligne+1,colonne-1]==1) and  (Image[ligne+1,colonne+1]==0):
                    #ligne actuelle
                    if Image[ligne,colonne-1]==1 and Image[ligne,colonne]==1 and Image[ligne,colonne]==0:
                        resultat[ligne,colonne]=0
               
    return resultat