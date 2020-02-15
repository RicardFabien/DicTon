'''
Created on 12 févr. 2020

@author: farben
'''

import os

class textReader():
    
    def __init__(self):
        pass
        
       
    def read(self, text, repetition):
        os.system("espeak '"+ text +"'")