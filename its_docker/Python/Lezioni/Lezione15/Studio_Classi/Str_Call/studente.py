from persona2 import Persona

'''

attributi della classe studente:
self.matricola: str

'''

#inizializzar 
class Studente(Persona):
    
    def __init__(self, name: str, lastname: str, age: int, matricola: str):
        
        #inizializzare la classe Persona richiamando il metodo init della superclasse
        super().__init__(name, lastname, age)
        self.setMatricola(matricola)
        
    def setMatricola(self, matricola: str):
        
        if matricola:
        
            self.matricola = matricola
            
        else:
            
            print("Errore... la matricola non può essere vuota")
            
    def getMatricola(self):
        
        return self.matricola
    
    #ridefinire il metodo __str__
    def __str__(self) -> str:
        
        return super().__str__() + f"\nMatricola: {self.getMatricola()}"
    
    def speak(self) -> str:
        
        return f"Hello my name is: {self.getName()}"