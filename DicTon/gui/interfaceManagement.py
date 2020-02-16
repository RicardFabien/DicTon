'''
Created on 30 janv. 2020

@author: farben
'''

from enum import Enum
from action.textReading import textReader
from files.fileManagement import getTextFromFile

class interfaceManager():
    
    def __init__(self):
        
        self.__textSource = "../default.txt"
        self.__text = getTextFromFile(self.__textSource)
        
        self.__textReader = textReader()
        
    
    def startReading(self):
        textReader.read(textReader, self.__text, 3)
    
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
    