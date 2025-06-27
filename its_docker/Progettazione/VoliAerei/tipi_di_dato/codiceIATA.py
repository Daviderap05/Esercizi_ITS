import re

class CodiceIATA:

    def __init__(self, codice: str):

        # Verifica che il codice IATA sia composto da 2 o 3 lettere maiuscole
        if not isinstance(codice, str):
            
            raise TypeError("Il codice IATA deve essere una stringa.")
        
        if not re.fullmatch(r"[A-Z]{2,3}", codice):
            
            raise ValueError("Codice IATA non valido, deve essere composto da 2 o 3 lettere maiuscole.")
        
        self.codice = codice
        
    def __str__(self):
        
        # Rappresentazione del codice IATA come stringa
        return f"{self.codice}"
    
    def __eq__(self, other):
        
        if isinstance(other, CodiceIATA):
            
            # Confronto tra due oggetti CodiceIATA
            return self.codice == other.codice
        
        return False

    def __hash__(self):
        
        # Hash del codice IATA per l'uso in strutture dati come set o dizionari
        return hash(self.codice)