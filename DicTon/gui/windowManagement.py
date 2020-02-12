'''
Created on 30 janv. 2020

@author: farben
'''

from tkinter import *
from gui.interfaceManagement import interfaceManager
'''Considered as false by eclipse, runs without problem'''



#The class organise the modification on the screen

class windowManager:
    
    interfaceManager = 0
  
    
  
    def __init__(self, interfaceManager):
        
        self.rootWindow = Tk()
        self.interfaceManager = interfaceManager

        
        self.rootWindow.title("DicTon")
        self.rootWindow.geometry("480x360")
        self.rootWindow.minsize(480,360)
        self.rootWindow.config(background = "#dfff80")
        
        
        
        
        def submitExercise():
            self.interfaceManager.submitExercise(self.textBox.get("1.0","end-1c"))
        
        buttonFrame = Frame()
        buttonFrame.pack(side = BOTTOM)
        
        button = Button(self.rootWindow, text = "Soumettre dictée", command = submitExercise)
        button.pack(side = BOTTOM)
        
        
        
        
        textFrame = Frame(self.rootWindow)
        textFrame.pack(fill = BOTH, side = TOP)
        
        self.textBox = Text(textFrame)
        self.textBox.pack(fill = BOTH, expand = YES)
        
        
        
        
        menubar = Menu(self.rootWindow)
        
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Choisir texte")
        menubar.add_cascade(label="Fichier", menu=menu1)
        
        
        
        self.rootWindow.config(menu = menubar)
        
        
        self.rootWindow.mainloop()
        

    


