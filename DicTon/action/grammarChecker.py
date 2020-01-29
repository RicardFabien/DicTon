'''
Created on 24 janv. 2020

@author: farben
'''

rawLines = [""]


while rawLines[len(rawLines) - 1] != "$" :
        
        line = input().strip()
        if line != "":
            rawLines.append(line)

rawLines.pop(0)
rawLines.pop()

for line in rawLines : 
    line = str.replace(",", "") 
    line = str.replace(".", "")
    line = str.replace(";", "") 
    line = str.replace(":", "")  

print(rawLines)

def getWordList():
    treatedLine = rawLines
    treatedLine