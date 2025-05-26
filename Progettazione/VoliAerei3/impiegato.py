from datetime import date
from custom_types import RealGEZ


class Impiegato():
    
    _nome: str
    _cognome: str
    _nascita: date
    _stipendio: RealGEZ
    
    
    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ) -> None:
        
        self._nome = nome
        self._cognome = cognome
        self._nascita = nascita
        self._stipendio = stipendio
        
        
    def __str__(self) -> str:
        
        return f"Nome: {self._nome}, Cognome: {self._cognome}, Data nascita: {self._nascita}, Stipendio: {self._stipendio}"
    
    
    def set_nome(self, new_nome) -> None:
        
        self._nome = new_nome   
    
    
    def get_nome(self) -> str:
        
        return self._nome
    
    
    def set_cognome(self, new_cognome) -> None:
        
        self._cognome = new_cognome
        
        
    def get_cognome(self) -> str:
        
        return self._cognome
    
    
    def get_nascita(self) -> date:
        
        return self._nascita
    
    
    def set_stipendio(self, new_stipendio) -> None:
        
        self._stipendio = new_stipendio
        
        
    def get_stipendio(self) -> RealGEZ:
        
        return self._stipendio