import re

class CodiceIATA:
    
    codice: str = ""

    def __init__(self, codice: str):

        check = re.fullmatch(r"[A-Z]{2,3}", codice)
        
        if check is None:
            
            raise ValueError("Codice IATA non valido, deve essere composto da 2 o 3 lettere maiuscole")
        
        self.codice = check.group(0)

    def __str__(self):
        
        return self.codice