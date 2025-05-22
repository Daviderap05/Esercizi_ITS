import re

class DurataVolo:
    
    def __init__(self, durata: str):
        
        # Verifica che la durata sia nel formato HH:MM:SS
        if not isinstance(durata, str):
            
            raise TypeError("La durata deve essere una stringa.")
        
        if not re.fullmatch(r"\d+:(?:[01]\d|2[0-3]):[0-5]\d", durata):
            
            raise ValueError("Durata non valida, deve essere nel formato HH:MM:SS.")
        
        self.durata = durata

    def __str__(self):
        
        # Rappresentazione della durata come stringa
        return f"{self.durata}"