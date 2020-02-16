'''
Created on 12 févr. 2020

@author: farben
'''

import os
import re

class textReader():
    
    def __init__(self):
        pass
        
       
    def read(self, text, repetition):
        
        print(text)
        
        parsedText = re.split("[,.]",text  )
        for p in parsedText :
            for i in range(repetition) :
                os.system("espeak '"+ p +"'")
                
                
        