from typing import Any

def inv(lista: list[Any]):
    
    #return lista[-1::-1]
    if not lista:
        return []
    return [lista[-1]] + inv(lista[:-1])
        
    
lista1: list[int] = [1, 2, 3, 4, 5]
lista2: list[str] = ["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"]

print(inv(lista1))
print(inv(lista2))