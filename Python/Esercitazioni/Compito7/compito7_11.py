import re
from string import punctuation

def count_unique_words(testo: str = "") -> str|dict[str, int]:
    
    if testo == "" or not isinstance(testo, str):
        
        return "Errore... inserire un testo."
    
    parole: list = list(filter(None, re.split(r'\W+', testo.lower()))) 
    diz: dict[str, int] = {}
    
    for p in parole:
        
        if p not in diz:
            
            diz[p] = 1
            
        else:
            
            diz[p] += 1
            
    return diz


#esercizio Professore non copre casi limite
def count_unique_words2(testo: str = "") -> str|dict[str, int]:
    
    testo = testo.lower()
    tokens: list[str] = testo.split(" ")
    diz: dict[str, int] = {}
    
    for token in tokens:
        
        token = token.strip(punctuation)
        
        if not token:
            
            continue
        
        elif token not in diz:
            
            diz[token] = 1
            
        else:
            
            diz[token] += 1
            
    return diz


print(count_unique_words("Hello, world! Hello... PYTHON? world."))
print(count_unique_words("Ciao!come stai."))
