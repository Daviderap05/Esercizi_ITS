# Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
# Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".

# Il metodo getArea() deve calcolare l'area del quadrato.

# Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore. 
# Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. 
# Vedi Esempio di output)


from Forma import Forma


class Quadrato(Forma):
    
    forma: str = "Quadrato"
    
    def __init__(self, nome: str, lunghezza: int):
        super().__init__(nome)
        
        if lunghezza > 1 and isinstance(lunghezza, int):
            self.lunghezza = lunghezza
        else:
            raise ValueError ("Inserire un numero valido > 0")
        
        
    def getArea(self):
        return self.lunghezza**2
    
    def Render(self):
        
        print("* " * self.lunghezza)
        
        for _ in range(self.lunghezza - 2):
            print("* " + "  " * (self.lunghezza - 2) + "*")
            
        print("* " * self.lunghezza)
        
        
q = Quadrato("q", 5)
q.Render()