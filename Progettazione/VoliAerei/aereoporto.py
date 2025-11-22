from Progettazione.VoliAerei.tipi_di_dato.codiceIATA import CodiceIATA

class Aereoporto:
    
    def __init__(self, codiceIATA: CodiceIATA, nome: str) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError ("Nome non valido")
        
        if not codiceIATA or not isinstance(codiceIATA, CodiceIATA):
            
            raise ValueError ("Codice IATA non valido")
        
        self.codiceIATA = codiceIATA
        self.setNome(nome)
        
    def __str__(self) -> str:
        
        return f"Nome aereoporto: {self.nome}, (codiciIATA - {self.codiceIATA})"
    
    def getNome(self) -> str:
        
        return self.nome
    
    def getCodiceIATA(self) -> CodiceIATA:
        
        return self.codiceIATA
    
    def setNome(self, nome: str) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError("Nome non valido")
        
        self.nome = nome