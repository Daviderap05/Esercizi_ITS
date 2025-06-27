def vowelsCounter(frase: str):

    if not frase:
        
        return 0
    
    else:
        
        return (frase[0].lower() in "aeiou") + vowelsCounter(frase[1:])

print(vowelsCounter("Ciao come stai"))