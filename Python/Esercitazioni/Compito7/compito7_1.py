# 1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
# la chiave è già presente, somma il valore al valore già associato alla chiave.


from typing import Any
def function1(lista: list) -> dict:
    
    diz: dict[Any, Any] = {}
    
    for key, value in lista:
        
        if key in diz:
            
            diz[key] += value
            
        else:
            
            diz[key] = value
            
    return diz
    
lista: list = [
    (1, 2),
    (2, 4),
    (3, 5),
    (1, 6),
    (2, 7)
]

print(function1(lista))