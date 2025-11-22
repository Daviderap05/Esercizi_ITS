class Nazione:
    
    def __init__(self, nome: str) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError ("Nome non valido")
        
        self.setNome(nome)
        
    def __str__(self) -> str:
        
        return f"nome nazione - {self.nome}"
    
    def getNome(self) -> str:
        
        return self.nome
    
    def setNome(self, nome: str) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError("Nome non valido")
        
        self.nome = nome