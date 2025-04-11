def vowelRemover(frase: str):

    if not frase:
        
        return ""
    
    else:
        
        return ("" if frase[0].lower() in "aeiou" else frase[0]) + vowelRemover(frase[1:])
    
print(vowelRemover("Ciao come stai"))