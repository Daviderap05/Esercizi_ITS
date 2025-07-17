from abc import ABC, abstractclassmethod, abstractmethod
from mytipes import *
from datetime import date
class Utente(ABC):

    _username: str # mutabile, noto alla nascita
    _registrazione: date # immutabile, noto alla nascita

    # abstractmethod
    def __init__(self, username: str, registrazione: date) -> None:
        self.set_username(username)
        self._registrazione = registrazione

    def username(self) -> str:
        return self._username

    def set_username(self, username: str) -> None:
        # controllo che il nome non sia gia stato usato
        self._username = username

    def registrazione(self) -> date:
        return self._registrazione

    







