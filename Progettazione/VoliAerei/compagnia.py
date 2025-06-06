from Progettazione.VoliAerei.città import Città
from Progettazione.VoliAerei.tipi_di_dato.anno import Anno


class CompagniaAerea:
    
    def __init__(self, nome: str, anno_fondazione: Anno, città: Città) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError ("Nome non valido")
        
        if not anno_fondazione or not isinstance(anno_fondazione, Anno):
            
            raise ValueError ("Anno di fondazione non valido")
        
        if not città or not isinstance(città, Città):
            
            raise ValueError ("Città non valida")
        
        self.setNome(nome)
        self.anno_fondazione = anno_fondazione
        self.setCittà(città)
        
    def __str__(self) -> str:
        
        return f"Nome compagnia aerea: {self.nome}, anno di fondazione - {self.anno_fondazione}, città - {self.getCittà()}"
    
    def getNome(self) -> str:
        
        return self.nome
    
    def getAnnoFondazione(self) -> Anno:
        
        return self.anno_fondazione
    
    def setNome(self, nome: str) -> None:
        
        if not nome or not isinstance(nome, str):
            
            raise ValueError("Nome non valido")
        
        self.nome = nome
        
    
    def setCittà(self, città: Città) -> None:
        
        if not città or not isinstance(città, Città):
            
            raise ValueError("Città non valida")
        
        self.città = città
        
    def getCittà(self) -> Città:
        
        return self.città