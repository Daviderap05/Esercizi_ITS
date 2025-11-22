import re

class CodiceVolo:
    
    def __init__(self, codice: str):
        
        # Verifica che il codice volo sia composto da 2 lettere maiuscole, uno spazio e da 1 a 4 cifre
        if not isinstance(codice, str):
            
            raise TypeError("Il codice volo deve essere una stringa.")
        
        if not re.fullmatch(r"[A-Z]{2} \d{1,4}", codice.upper().strip()):
            
            raise ValueError("Codice volo non valido, deve essere composto da 2 lettere maiuscole seguite da uno spazio e da 1 a 4 cifre.")
        
        self.codice = codice

    def __str__(self):
        
        # Rappresentazione del codice volo come stringa
        return f"{self.codice}"

    def __hash__(self):
        
        # Hash del codice volo per l'uso in strutture dati come set o dizionari
        return hash(self.codice)