'''
Created on 30 janv. 2020

@author: farben
'''

from enum import Enum
from action.textReading import textReader
from files.fileManagement import getTextFromFile

class interfaceManager():
    
    __textSource = "../default.txt"
    
    def __init__(self):
        
        self.__text = "Le petit lapin saute"
        self.__textReader = textReader()
        
    
    def startReading(self):
        self.__textReader.read( self.__text, 3)
        self.__textReader.start()
    
    
    def stopReading(self):
        self.__textReader.kill()
    
    
    def changeTextSource(self,path) : 
        
        self.__textSource = path
        self.__text = getTextFromFile(self.__textSource)
    
    
    def getText(self):
        return self.__text
    
    def submitExercise(self, text):
        
        cutText = text.split()
        originalCutText = self.__text.split()
        
        missedWordCoor = []
        charCount = 0
        
        for i in enumerate(cutText) :
            if(cutText[i[0]] != originalCutText[i[0]]):
                missedWordCoor.append([charCount , charCount + len(cutText[i[0]])])
                
            charCount += len(cutText[i[0]])
            charCount += 1
            
        return missedWordCoor
            
            
        
        
         

    