import re

class CodiceVolo:
    
    codice: str

    def __init__(self, codice: str):

        match = re.fullmatch(r"[A-Z]{2} \d{1,4}", codice)

        if match is None:
            
            raise ValueError("Codice volo non valido, deve essere composto da 2 lettere maiuscole seguite da uno spazio e da 1 a 4 cifre")
        
        self.codice = match.group(0)

    def __str__(self):
        
        return self.codice

    def __eq__(self, other):
        
        if isinstance(other, CodiceVolo):
            
            return self.codice == other.codice
        
        return False

    def __hash__(self):
        
        return hash(self.codice)