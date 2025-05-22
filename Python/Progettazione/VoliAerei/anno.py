import re

class Anno:
    def __init__(self, anno: str):
        
        # Verifica che l'anno sia compreso tra 1900 e 2199
        if not isinstance(anno, str):
            
            raise TypeError("L'anno deve essere una stringa.")
        
        if not re.fullmatch(r"19\d\d|2[0-1]\d\d", anno):
            
            raise ValueError("Anno non valido, deve essere compreso tra 1900 e 2199.")
        
        self.anno = anno

    def __str__(self):
        
        # Rappresentazione dell'anno come stringa
        return f"{self.anno}"