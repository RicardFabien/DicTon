'''
Created on 15 févr. 2020

@author: farben
'''

import os

def getTextFromFile(path) :
    
    content = ""
    
    if not os.path.isfile(path):
        print('File does not exist.')
    
    else :
        with open(path) as f :
            contentList = f.read().splitlines()
        for line in contentList :
            content += " " +line 
            
        return content
    

        
