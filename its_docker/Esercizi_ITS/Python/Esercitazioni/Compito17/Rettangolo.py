# Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa 
# la lunghezza della sua base e della sua altezza.

# Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo,
# ed impostare il nome della forma su "Rettangolo".

# Il metodo getArea() deve calcolare l'area del rettangolo.

# Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
# Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)


from Forma import Forma


class Rettangolo(Forma):
    
    forma: str = "Rettangolo"
    
    def __init__(self, nome: str, base: int, altezza: int) -> None:
        super().__init__(nome)
        
        if isinstance(base, int) and base > 1:
            self.base = base
        else:
            raise ValueError ("Inserire una base valida > 0")
        
        if isinstance(altezza, int) and altezza > 1:
            self.altezza = altezza
        else:
            raise ValueError ("Inserire un'altezza valida > 0")
        
        
    def getArea(self) -> None:
        print (f"\n{self.base * self.altezza}")
    
    
    def Render(self) -> None:
        
        print("* " * self.base)
        
        for _ in range(self.altezza - 2):
            print("* " + "  " * (self.base - 2) + "*")
            
        print("* " * self.base)
        
        
r = Rettangolo ("r", 5, 2)
r.Render()
r.getArea()