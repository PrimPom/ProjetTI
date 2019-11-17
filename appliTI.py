# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 15:37:34 2019

@author: primp
"""

from numpy import arange, sin, pi

import matplotlib

# uncomment the following to use wx rather than wxagg
matplotlib.use('WX')
#from matplotlib.backends.backend_wx import FigureCanvasWx as FigureCanvas

# comment out the following to use wx rather than wxagg
#matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

from matplotlib.backends.backend_wx import NavigationToolbar2Wx

from matplotlib.figure import Figure

import wx.lib.mixins.inspection as WIT


import wx
from seuillageImage import seuillageImage
from niveauDegris import imageEnNiveauDeGris

APP_EXIT = 1
APP_SEUILLAGE=2
APP_ADDITION=3
APP_SOUSTRACTION=4
APP_EROSION=5
APP_DILATATION=6
global newfile
"""from PIL import Image

from skimage.exposure import histogram

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np"""

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
from comparateur import comparateurDeTailleDimage

from PIL import Image

from skimage.exposure import histogram

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np




class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        
        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour("gray")
        
        #PREMIER menu bar
        fileMenu = wx.Menu()
        #fileMenu.Append(wx.ID_NEW, '&New')
        #fileMenu.Append(wx.ID_OPEN, '&Charger une image')
        #fileMenu.Append(wx.ID_SAVE, '&Enregistrer')
        
        qmiLoad = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Charger une image')
        qmiLoad.SetBitmap(wx.Bitmap('images/picture.png'))
        fileMenu.Append(qmiLoad)
        
        
        qmiSave = wx.MenuItem(fileMenu, wx.ID_SAVE, '&Enregistrer\tCtrl+S')
        qmiSave.SetBitmap(wx.Bitmap('images/diskette.png'))
        fileMenu.Append(qmiSave)
        
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quitter\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('images/logout.png'))
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)

        menubar.Append(fileMenu, '&Fichier')
        
        
          #Deuxieme menu bar
        fileMenu2 = wx.Menu()
        fileMenu2.Append(APP_SEUILLAGE, '&Seuillage d\'une image')
        fileMenu2.Append(APP_ADDITION, '&Addition de deux images')
        fileMenu2.Append(APP_SOUSTRACTION, '&Soustraction de deux images')
        fileMenu2.AppendSeparator()
        
        eros = wx.Menu()
        eros.Append(wx.ID_ANY, 'Structurant Cercle')
        eros.Append(wx.ID_ANY, 'Structurant Carré')
        fileMenu2.AppendMenu(wx.ID_ANY, '&Erosion d\'image ', eros)
        
        dilat = wx.Menu()
        dilat.Append(wx.ID_ANY, 'Structurant Cercle')
        dilat.Append(wx.ID_ANY, 'Structurant Carré')
        

        fileMenu2.AppendMenu(wx.ID_ANY, '&Dilatation d\'image ', dilat)
        
        self.Bind(wx.EVT_MENU, self.OnSeuillage, id=APP_SEUILLAGE)
        self.Bind(wx.EVT_MENU, self.OnAddition, id=APP_ADDITION)
       
        menubar.Append(fileMenu2, '&Opérations Simples')
        
        
              #Troisieme menu bar
        fileMenu3 = wx.Menu()
            
        ouvert = wx.Menu()
        ouvert.Append(wx.ID_ANY, 'Structurant Cercle')
        ouvert.Append(wx.ID_ANY, 'Structurant Carré')
        fileMenu3.AppendMenu(wx.ID_ANY, '&Ouverture d\'une image ', ouvert)
        
        ferme = wx.Menu()
        ferme.Append(wx.ID_ANY, 'Structurant Cercle')
        ferme.Append(wx.ID_ANY, 'Structurant Carré')
        fileMenu3.AppendMenu(wx.ID_ANY, '&Fermeture d\'une image ', ouvert)
        fileMenu3.AppendSeparator()
        fileMenu3.Append(APP_ADDITION, '&Amincissement')
        fileMenu3.Append(APP_SOUSTRACTION, '&Epaississement')
            
        menubar.Append(fileMenu3, '&Opérations Complexes')
        
                      #Quatrieme menu bar
        fileMenu4 = wx.Menu()
        fileMenu4.Append(APP_ADDITION, '&Squellete par Lantuejoul')
        fileMenu4.Append(APP_SOUSTRACTION, '&Squellette par amincissement homotopique')         
        menubar.Append(fileMenu4, '&Opérations Avancées')

        self.SetMenuBar(menubar)     
        self.SetSize((1000, 600))
        self.SetTitle('AppliTI')
        self.Centre()
        
    def OnQuit(self, e):
        self.Close()
        
    def OnOpen(self, event):
        
        # Create open file dialog
        openFileDialog = wx.FileDialog(self, "Open", "", "", 
                                       "PNG files (*.png)|*.png", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        global newfile
        newfile=openFileDialog.GetPath()
        global image,imageTableau
        image=Image.open(newfile)
        
        #Transformation de l'image en tableau
        imageTableau = np.asarray(image)
        print(openFileDialog.GetPath())
        
        
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap(openFileDialog.GetPath(), wx.BITMAP_TYPE_ANY))
        openFileDialog.Destroy()
        self.mincol.SetPosition((40, 160))
        
        imgORIG = wx.Image(newfile, wx.BITMAP_TYPE_ANY)
        global  resultat
        resultat = imgORIG.ConvertToBitmap()
        
    def OnSeuillage(self, e):
        imageSeuille=seuillageImage(imageTableau,0.5)
     
        img=Image.fromarray(imageSeuille)      
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
       
        #Ca fait sortir une fenetre figure
        plt.figure(figsize=(8,8))
        plt.imshow(imageSeuille,cmap='gray')
        
        """
        mpimg.imsave("imageSeuille.png", imageEnNiveauDeGris(imageSeuille))
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY,
            wx.Bitmap('imageSeuille.png', wx.BITMAP_TYPE_ANY))
        
        self.mincol.SetPosition((160, 160))"""
        
    def OnAddition(self, e):
        imageSeuille=seuillageImage(imageTableau,0.5)
        
        #Transformation de l'image en tableau
        imageAadditionner = self.ouvertureDialog()    
        
        imageSeuille2=seuillageImage(imageAadditionner,160)
        
        if comparateurDeTailleDimage(imageSeuille,imageSeuille2)==1:
            addition=additionImage(imageSeuille,imageSeuille2)
        
            self.figure = Figure()
            self.axes = self.figure.add_subplot(111)     
            #Ca fait sortir une fenetre figure
            plt.figure(figsize=(8,8))
            plt.imshow(addition,cmap='gray')
        else:
            self.showMessage(self)
         
     
   
        
    def showMessage(self):
        wx.MessageBox('Les deux images n\'ont pas la même taille ','Erreur Addition',
            wx.OK | wx.ICON_ERROR)       

        
    def ouvertureDialog(self):
        #Creation d'une boite de selection pour l'image
        openFileDialog = wx.FileDialog(self, "Open", "", "", 
                                       "PNG files (*.png)|*.png", 
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()       
        fichierAadditionner=openFileDialog.GetPath()      
        image=Image.open(fichierAadditionner)     
        #Transformation de l'image en tableau
        imageArray = np.asarray(image)
        openFileDialog.Destroy()
        
        return imageArray

       




def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()