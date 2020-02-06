'''
Created on 30 janv. 2020

@author: farben
'''

from enum import Enum

class InterfaceManager():
    
    def __init__(self):
        pass
    
    def SubmitExercise(self):
        print("soumet dictée")   


class commands(Enum):
    SUBMIT = "submit"
    START_SPEECH = "start_speech"
    
    