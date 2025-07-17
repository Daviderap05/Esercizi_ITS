from utente import Utente
from mytipes import *
from datetime import date
from bid_ut import bid_ut

# eredita da utente ... classe astratta
class Privato(Utente):

    _bid_effettuati: dict[Bid, bid_ut._link] # da associazione [0..*]

    def __init__(self, username: str, registrazione: date) -> None:
        super().__init__(username, registrazione)

    def _add_link_bid_ut(self, l: bid_ut._link) -> None:
        # nel caso provi a chiamare un link in cui non e conivolto 
        if l.privato() is not self:
            raise ValueError('Il link non mi coin')

        # se provi a creare lo stessos link 2 volte
        if l.bid() in _bid_effettuati:
            raise KeyError('Non si puo effettuare lo stesso bid 2 volte')

        # lo aggiungo tra i bid effettuati dall'utente
        self._bid_effettuati[l.bid()] = l

    
    

    