'''
Created on 29 janv. 2020

@author: farben'''



def getRawText() :
    rawLines = ""
    while True:    
        line = input()
        rawLines += line + "\n"
    
        if line.strip() == "$" :
            return rawLines
    
print(getRawText())