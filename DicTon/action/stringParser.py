'''
Created on 29 janv. 2020

@author: farben
'''
def parseText():
    rawLines = []


   
    
    rawLines.pop(0)
    rawLines.pop()
    
    for line in rawLines : 
        print(rawLines)
        line = line.replace(",", "") 
        line = line.replace(".", "")
        line = line.replace(";", "") 
        line = line.replace(":", "")  
    
    print(rawLines)
    return  rawLines
    