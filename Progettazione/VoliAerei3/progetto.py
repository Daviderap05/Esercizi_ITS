from custom_types import RealGEZ


class Progetto():
    
    _nome: str
    _budget: RealGEZ
    
    
    def __init__(self, nome: str, budget: RealGEZ) -> None:

        self._nome = nome
        self._budget = budget
        
        
    def __str__(self) -> str:
        
        return f"Nome: {self._nome}, Budget: {self._budget}"
    
    
    def set_nome(self, new_nome) -> None:
        
        self._nome = new_nome   
    
    
    def get_nome(self) -> str:
        
        return self._nome
    
    
    def set_budget(self, new_budget) -> None:
        
        self._budget = new_budget  
    
    
    def get_budget(self) -> RealGEZ:
        
        return self._budget