from abc import ABC, abstractmethod
from datetime import date


class Utente(ABC):

    username: str # mutabile, noto alla nascita
    registrazione: date # immutabile, noto alla nascita

    @abstractmethod
    def __init__(self, username: str, registrazione: date) -> None:
        self.setUsername(username)
        self.registrazione = registrazione

    def setUsername(self, username: str) -> None:
        self.username = username
        
    def getUsername(self) -> str:
        return self.username

    def getRegistrazione(self) -> date:
        return self.registrazione