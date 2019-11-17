# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 08:30:28 2019

@author: primp
"""

#Importation des différentes fonctions du projet 
from binarisation import binarisation
from histogramm import histogramme
from niveauDegris import imageEnNiveauDeGris
from seuillageImage import seuillageImage
from additionImage import additionImage
from soustractionImage import soustractionImage
from erosionImage import erosionImage
from dilatationImage import dilatationImage
from ouvertureImage import ouvertureImage
from fermetureImage import fermetureImage
from aminciHuConnexite import aminciHuConnexite
from epaiciHuConnexite import epaiciHuConnexite
from tourCompletAminci import tourCompletAminci 
from homothopique import homothopique

from PIL import Image

from skimage.exposure import histogram

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np



#Lecture image couleur Granule1.bmp:
im_in_granule = Image.open("segment.png")
#Transformation de l'image en tableau
im_color_granule = np.asarray(im_in_granule)

#imageGrise=imageEnNiveauDeGris(im_color_granule)
imageSeuille1=seuillageImage(imageEnNiveauDeGris(im_color_granule),1)
imageSeuille2=seuillageImage(imageEnNiveauDeGris(im_color_granule),167)
aAfficher=tourCompletAminci(imageSeuille1)

#Affichage image:
plt.figure(figsize=(10,10))
plt.imshow(imageSeuille1,cmap='gray')

plt.figure(figsize=(10,10))
plt.imshow(aAfficher,cmap='gray')

plt.figure(figsize=(10,10))
plt.imshow(homothopique(imageSeuille1),cmap='gray')