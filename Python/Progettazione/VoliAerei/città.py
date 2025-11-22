class Città:
    
    def __init__(self, nome: str, n_abitanti: int) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError ("Nome non valido")
        
        if not n_abitanti or not isinstance(n_abitanti, int) or n_abitanti < 0:
            
            raise ValueError ("n_abitanti non valido, deve essere un intero positivo o guale a 0")
        
        self.setNome(nome)
        self.setN_abitanti(n_abitanti)
        
    def __str__(self) -> str:
        
        return f"Nome città: {self.nome}. Il numero dei suoi abitanti è {self.n_abitanti}"
    
    def getNome(self) -> str:
        
        return self.nome
    
    def getN_abitanti(self) -> int:
        
        return self.n_abitanti
    
    def setNome(self, nome: str) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError("Nome non valido")
        
        self.nome = nome
        
    def setN_abitanti(self, n_abitanti: int) -> None:
        
        if not n_abitanti or not isinstance(n_abitanti, int) or n_abitanti < 0:
            
            raise ValueError("n_abitanti non valido, deve essere un intero positivo o guale a 0")
        
        self.n_abitanti = n_abitanti