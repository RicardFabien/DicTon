'''
Created on 12 févr. 2020

@author: farben
'''

import os
import re
import threading
from time import sleep
from gi import sys

class textReader(threading.Thread):
    
    __text = ""
    __repetition = 1
    
    __stopEvent = threading.Event()
    __sentencePart = 0
    
    def __init__(self):
        threading.Thread.__init__(self)
        
       
    def read(self, text, repetition):
        self.__text = text
        self.__repetition = repetition
        self.__sentencePart = 0
        
                     
    def kill(self):
        self.__stopEvent.set()
    
                     
    def run(self):
        
        parsedText = re.split("[,.]",self.__text  )
        
        for p in parsedText :
            
            for i in range(self.__sentencePart, self.__repetition) :
                os.system("espeak -v fr '"+ p +"'")
                sleep(1)
                self.__sentencePart += 1
                
                if(self.__stopEvent.is_set()):
                    break
        