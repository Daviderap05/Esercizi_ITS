'''
Di una persona dobbiamo sapere delle informazioni.
Queste informazioni vengono chiamate attributi ( della classe Persona).
Le infrmazioni saranno:

- nome
- cognome
- età

Come li rappresento i python?

self.nome: str (attributo di tipo stringa)
self.cognome: str (attributo di tipo stringa)
self.eta: int (attributo di tipo intero)
'''

class Persona:
    
    #Costrutture della classe Persona
    
    def __init__(self, nome: str, cognome: str, eta: int):
        
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
    
    #funzione che mostri in output tutti i dati di una persona
    
    def mostra_dati(self) -> None:
        
        print(f"Nome: {self.nome}\ncognome: {self.cognome}\netà: {self.eta}")
    
if __name__ == "__main__":

    d: Persona = Persona("Davide", "Raponi", 19)

    d.mostra_dati()