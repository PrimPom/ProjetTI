# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:20:34 2019

@author: primp
"""
from tourCompletAminci import tourCompletAminci
def homothopique(Image):
    resultat = tourCompletAminci(Image)
    resultatSuivant=tourCompletAminci(resultat)
    
    while (resultatSuivant == resultat).all ==False :
        #tampon=resultatSuivant
        resultat=resultatSuivant
        resultatSuivant=tourCompletAminci(resultatSuivant)
      
    return resultat