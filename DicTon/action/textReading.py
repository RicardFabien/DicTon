'''
Created on 12 févr. 2020

@author: farben
'''

import os

class textReader():
    
    def __init__(self, text):
        self.text = text
        
       
    def read(self):
         os.system("espeak '"+ self.text +"'")