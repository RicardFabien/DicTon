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
        
        self.__textSource = "../default.txt"
        self.__text = getTextFromFile(self.__textSource)
        
        self.__textReader = textReader()
        
    
    def startReading(self):
        self.__textReader.read( self.__text, 3)
        self.__textReader.start()
    
    def stopReading(self):
        pass
    
    def changeTextSource(self,path) : 
        pass
    
    
    
    def submitExercise(self, text):
        print("soumet dictée " + text)   


class commands(Enum):
    SUBMIT = "submit"
    START_SPEECH = "start_speech"
    PAUSE_SPEECH = "pause_speech"
    