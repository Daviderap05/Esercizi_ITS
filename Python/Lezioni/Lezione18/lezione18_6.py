import random, string

def genera_stringa_casual(lunghezza: int):
    
    caratteri: str = string.ascii_letters + string.digits + string.punctuation
    ris: str = ""
    
    for i in range(lunghezza):
        
        ris += (random.choice(caratteri))
    
    return ris

lunghezza_desiderata: int = 10

stringa_casuale: str = genera_stringa_casual(lunghezza_desiderata)
print(stringa_casuale)