'''
Created on 29 janv. 2020

@author: farben
'''


def removeCharacters (text): 
    
        text = text.replace(",", " ") 
        text = text.replace(".", " ")
        text = text.replace(";", " ") 
        text = text.replace(":", " ")
        
        return text


def simpleParseText(text):

        text = removeCharacters(text)
        
        cutText = text.split()
        
        return  cutText





def complexParseText (text) :
    
        text = removeCharacters(text)
        
        cutText = text.split("\n")
        
        
        for line in enumerate(cutText) :
                cutText[line[0]] = cutText[line[0]].split()
    
        return  cutText

    