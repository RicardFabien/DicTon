'''
Created on 30 janv. 2020

@author: farben
'''

from enum import Enum
from gui.textReading import textReader

class interfaceManager():
    
    def __init__(self):
        
        self.textSource = "default.txt"
        self.__textReader = textReader()
        
    
    def startReading(self):
        pass
    
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
    