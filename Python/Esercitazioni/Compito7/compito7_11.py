import re

def count_unique_words(testo: str = "") -> str|dict[str, int]:
    
    if testo == "":
        
        return "Errore... inserire un testo."
    
    parole: list = list(filter(None, re.split(r'\W+', testo.lower()))) 
    diz: dict[str, int] = {}
    
    for p in parole:
        
        if p not in diz:
            
            diz[p] = 1
            
        else:
            
            diz[p] += 1
            
    return diz


print(count_unique_words("Hello, world! Hello... PYTHON? world."))