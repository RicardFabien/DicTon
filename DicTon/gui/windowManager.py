'''
Created on 30 janv. 2020

@author: farben
'''

from tkinter import *
from tkinter.messagebox import *

def alert():
    showinfo("alerte", "Bravo!")

class windowManager:
    
    interfaceManager = 0
  
    def __init__(self,rootWindow = Tk()):
        rootWindow = rootWindow
        
        
        rootWindow.title("DicTon")
        rootWindow.geometry("480x360")
        rootWindow.minsize(480,360)
        rootWindow.config(background = "#dfff80")
        
        button = Button(rootWindow, text = "Soumettre dictée")
        button.pack(side = BOTTOM)
        
        
        menubar = Menu(rootWindow)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Choisir texte", command=alert)
        menubar.add_cascade(label="Fichier", menu=menu1)
        
        
        
        rootWindow.config(menu = menubar)
        
        
        rootWindow.mainloop()
        
windowManager = windowManager()


