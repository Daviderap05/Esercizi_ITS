# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float 
# che memorizza l'importo del pagamento e si definiscano appropriati metodi get() e set(). 

# L'importo non è un parametro da passare in input alla classe Pagamento ma deve essere 
# inizializzato utilizzando il metodo set() dove opportuno. 

# Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento, ad esempio: 
# "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

class Pagamento():
    
    def __init__(self) -> None:
        
        self.__importo: float = 0.0
    
    def setImporto(self, importo: float) -> None:
        if importo > 0 and isinstance(importo, float):
            self.__importo: float = importo
        else: 
            raise ValueError ("Errore, importo non valido")
    
    def getImporto(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento: {self.getImporto():2f}")