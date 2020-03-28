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
        
        self.__text = "Le petit lapin saute, \n Le renard le suit de près,\n la fleur tombe."
        self.__textReader = textReader()
        
    
    def startReading(self):
        self.__textReader.read( self.__text, 3)
        self.__textReader.start()
    
    
    def stopReading(self):
        self.__textReader.kill()
    
    
    def changeTextSource(self,path) : 
        
        self.__textSource = path
        self.__text = getTextFromFile(self.__textSource)
    
    
    def submitExercise(self, text):
        
        print("soumet dictée " + text)   

    