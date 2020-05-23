'''
Created on 30 janv. 2020

@author: farben
'''

from enum import Enum
from action.textReading import textReader
from files.fileManagement import getTextFromFile
from gui.stringParser import simpleParseText, removeCharacters
from symbol import except_clause

class interfaceManager():
    
    __textSource = "../default.txt"
    
    def __init__(self):
        
        self.__text = "Le petit lapin saute"
        self.__textReader = textReader()
        
    
    def startReading(self):
        self.__textReader.read( self.__text, 3)
        self.__textReader.start()
    
    
    def stopReading(self):
        self.__textReader.kill()
    
    
    def changeTextSource(self,path) : 
        
        self.__textSource = path
        self.__text = getTextFromFile(self.__textSource)
    
    
    def getText(self):
        return self.__text
    
    def submitExercise(self, text):
        
        cutText = simpleParseText(text)   
        originalCutText = simpleParseText(self.__text)
        
        missedWords = []
        
        for i in enumerate(cutText) :
            
            if((i[0]) >= len(originalCutText)) :
                break
            #print(cutText[i[0]] + " " + originalCutText[i[0]])
            if(cutText[i[0]] != originalCutText[i[0]]):
                missedWords.append(cutText[i[0]])
        
        print("missedWords : ")    
        print( missedWords)
        
        originalText = text.split("\n")
        print("original text : ")
        print(originalText)    
            
        missedWordCoor = []   
        line = 1
        
            
        for word in missedWords :
            while (line - 1 < len(originalText)):
                try:
                    wordIndex = originalText[line - 1].index(word)
                    missedWordCoor.append([wordIndex,(wordIndex + len(word)),line])
                    break
                except:
                    line += 1
                
            
                   

        return missedWordCoor
        
        
        
         

    