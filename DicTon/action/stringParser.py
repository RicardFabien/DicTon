'''
Created on 29 janv. 2020

@author: farben
'''
def parseText(text):

    text = text.replace(",", " ") 
    text = text.replace(".", " ")
    text = text.replace(";", " ") 
    text = text.replace(":", " ") 
    
    rawLines = text.split()

    print(rawLines)
    return  rawLines
    