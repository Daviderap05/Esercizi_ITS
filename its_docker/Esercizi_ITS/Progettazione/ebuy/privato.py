from utente import Utente
from datetime import date

# privato eredita da utente(classe astratta)
class Privato(Utente):

    def __init__(self, username: str, registrazione: date) -> None:
        super().__init__(username, registrazione)