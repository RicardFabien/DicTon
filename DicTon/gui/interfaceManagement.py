'''
Created on 30 janv. 2020

@author: farben
'''

from enum import Enum

class interfaceManager():
    
    def __init__(self):
        pass
    
    def submitExercise(self, text):
        print("soumet dictée " + text)   


class commands(Enum):
    SUBMIT = "submit"
    START_SPEECH = "start_speech"
    PAUSE_SPEECH = "pause_speech"
    