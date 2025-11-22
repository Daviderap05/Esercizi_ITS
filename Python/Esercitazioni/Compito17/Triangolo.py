# Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione 
# di un lato del triangolo (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).

# Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, 
# ed impostare il nome della forma su "Triangolo".

# Il metodo getArea() deve calcolare l'area del triangolo.

# Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza 
# pari ai valori passati nel costruttore. Il triangolo da stampare deve essere un triangolo 
# vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)
 
# Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette 
# di controllare come termina ogni chiamata a print, e impostandolo a uno spazio si può fare in modo 
# che tutte le stampe successive siano sulla stessa riga, separate da uno spazio.

from Forma import Forma


class Triangolo(Forma):
    
    forma: str = "Triangolo"
    
    def __init__(self, nome: str, lato: int) -> None:
        super().__init__(nome)
        
        if isinstance(lato, int) and lato > 2:
            self.lato = lato
        else:
            raise ValueError ("Inserire un lato valido > 0")

        
    def getArea(self) -> None:
        print (f"\n{(self.lato ** 2) / 2}")
    
    
    def Render(self) -> None:
        
        for i in range(self.lato):
            
            if i == 0:
                print("*")
                
            elif i < (self.lato - 1):
                print("* " + "  " * (i - 1) + "*")
                
            else:
                print("* " * self.lato)
        
        
t = Triangolo ("t", 8)
t.Render()
t.getArea()