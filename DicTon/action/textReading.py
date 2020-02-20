'''
Created on 12 févr. 2020

@author: farben
'''

import os
import re
import threading
from time import sleep

class textReader(threading.Thread):
    
    __text = ""
    __repetition = 1
    
    __pause = False
    __sentencePart = 0
    
    def __init__(self):
        threading.Thread.__init__(self)
        
       
    def read(self, text, repetition):
        self.__text = text
        self.__repetition = repetition

                     
    def pause(self):
        pass
    
                     
    def run(self):
        
        parsedText = re.split("[,.]",self.__text  )
        
        while self.__pause not in True :
            for p in parsedText :
                if(self.__pause):
                        break
                for i in range(self.__sentencePart, self.__repetition) :
                    os.system("espeak -v fr '"+ p +"'")
                    if(self.__pause):
                        break
                    sleep(1)
                self.__sentencePart += 1
        