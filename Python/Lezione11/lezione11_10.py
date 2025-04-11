def charDuplicator(parola):
    
    if not parola:
        
        return ""
    
    return parola[0] * 2 + charDuplicator(parola[1:])

print(charDuplicator("libro"))