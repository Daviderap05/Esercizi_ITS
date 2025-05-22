import re

class DurataVolo:
    
    durata: str

    def __init__(self, durata: str):

        pattern = re.fullmatch(r"\d+:(?:[01]\d|2[0-3]):[0-5]\d", durata)

        if pattern is None:
            
            raise ValueError("Durata non valida, deve essere nel formato HH:MM:SS")
        
        self.durata = pattern.group(0)

    def __str__(self):
        
        return self.durata