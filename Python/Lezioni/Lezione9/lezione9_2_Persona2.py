class Persona:
    
    def __init__(self):
        
        self.nome = ""
        self.cognome = ""
        self.eta = 0
        
    def setNome(self, nome: str) -> None:
        
        self.nome = nome
        
    def getNome(self) -> str:
        
        return self.nome
        
    def setCognome(self, cognome: str) -> None:
        
        self.cognome = cognome
        
    def getCognome(self) -> str:
        
        return self.cognome
        
    def setEta(self, eta: int) -> None:
        
        if 0 <= eta < 130:
            
            self.eta = eta
            
    def getEta(self) -> int:
        
        return self.eta
        
    def mostra_dati(self) -> None:
        
        print(f"Nome: {self.nome}\ncognome: {self.cognome}\netà: {self.eta}")
        

d: Persona = Persona()

d.setNome("Davide")
print(d.getNome())

d.setCognome("Raponi")
print(d.getCognome())

d.setEta(19)
print(f"{d.getEta()}\n")

d.mostra_dati()        