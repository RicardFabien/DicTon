'''
Created on 12 févr. 2020

@author: farben
'''

import os
import re
import threading

class textReader(threading.Thread):
    
    __text = ""
    __repetition = 1
    
    def __init__(self):
        threading.Thread.__init__(self)
        
       
    def read(self, text, repetition):
        self.__text = text
        self.__repetition = repetition
                     
    def run(self):
        
        parsedText = re.split("[,.]",self.__text  )
             
        for p in parsedText :
            for i in range(self.__repetition) :
                os.system("espeak '"+ p +"'")
        