# Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente 
# al nome della forma e le funzionalità base di ogni forma, come i metodi astratti getArea() 
# per calcolare l'area e render() per disegnare su schermo la forma.

from abc import *


class Forma(ABC):
    
    def __init__(self, nome: str) -> None:
        super().__init__()
        
        if nome and isinstance(nome, str):
            self.nome = nome
            
            
    @abstractmethod
    def getArea() -> None:
        pass
        
    
    @abstractmethod
    def Render() -> None:
        pass    
    