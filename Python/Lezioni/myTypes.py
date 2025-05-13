from typing import Self, Any
from enum import *


class Genere(StrEnum):
    
    uomo = auto()
    donna = auto()
    
class Continente(StrEnum):
    
    asia = auto()
    europa = auto()
    america = auto()
    africa = auto()
    antartide = auto()
    
    
class voto(int):
    
    def __new__(cls, v: int|float|Self) -> Self:
        
        if v < 18 or v > 30:
            
            raise ValueError(f"Value v == {v} must be between 18 and 30")
        
        return int.__new__(cls, v)
                
if __name__ == "__main__":
    
    print(Genere.uomo.upper())
    print(type(Genere.donna))
    
    print(Continente.asia.capitalize())