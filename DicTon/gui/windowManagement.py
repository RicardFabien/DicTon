'''
Created on 30 janv. 2020

@author: farben
'''

from tkinter import *  

from gui.interfaceManagement import interfaceManager
from tkinter.filedialog import  askopenfilename


#The class organises the modification on the screen

class windowManager:
    
    interfaceManager = 0
  
    def submitExercise(self):
            missedWord = self.interfaceManager.submitExercise(self.textBox.get("1.0","end-1c"))
            
            self.textBox.tag_configure( "MISS", foreground = "red" )
            self.textBox.tag_configure( "CORRECT", foreground = "green" )
            
            self.textBox.tag_add("CORRECT",SEL_FIRST,SEL_LAST)
            
            for coor in missedWord :
                self.textBox.tag_add("MISS", "1." + str(coor[0]), "1." + str(coor[1]))
            
            
            
            
  
    def startExercise(self):
        self.interfaceManager.startReading()
        
    def stopExercise(self):
        self.interfaceManager.stopReading()
    
    def changeTextSource(self):
        
        textSource = askopenfilename(initialdir = "/home",title = "Select file")
        self.interfaceManager.changeTextSource(textSource)
  
    def __init__(self, interfaceManager):
        
        self.rootWindow = Tk()
        self.interfaceManager = interfaceManager

        
        self.rootWindow.title("DicTon")
        self.rootWindow.geometry("480x360")
        self.rootWindow.minsize(480,360)
        self.rootWindow.config(background = "#dfff80")
        
        
        
        buttonFrame = Frame()
        buttonFrame.pack(side = BOTTOM)
        
        submitButton = Button(buttonFrame, text = "Soumettre dictée", command = self.submitExercise)
        submitButton.pack(side = RIGHT)
        
        startButton = Button(buttonFrame, text = "Commencer dictée", command = self.startExercise)
        startButton.pack(side = LEFT)
        
        pauseButton = Button(buttonFrame, text = "Stopper dictée", command = self.stopExercise)
        pauseButton.pack()
        
        
        textFrame = Frame(self.rootWindow)
        textFrame.pack(fill = BOTH, side = TOP, expand = YES)
        
        self.textBox = Text(textFrame)
        self.textBox.pack(fill = BOTH, expand = YES)
        
        
        
        
        menubar = Menu(self.rootWindow)
        
        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Choisir texte", command = self.changeTextSource)
        menubar.add_cascade(label="Fichier", menu=menu1)
        
        
        
        self.rootWindow.config(menu = menubar)
        
        def kill():
            self.interfaceManager.stopReading()
            sys.exit()
        
        
        self.rootWindow.protocol("WM_DELETE_WINDOW", kill)
        self.rootWindow.mainloop()
        




