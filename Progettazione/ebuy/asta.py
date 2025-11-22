from postoggetto import Postoggetto
from mytipes import *
from datetime import date



class Asta(Postoggetto):

    prezzo_bid: RealGZ # mutabile, noto alla nascita
    scadenza: date # immutabile, noto alla nascita

    def __init__(self, descrizione: str, anni_garanzia: IntGEZ, pubblicazione: date, prezzo: RealGEZ, is_nuovo: bool,\
                    prezzo_bid: RealGZ, scadenza: date, condizione: Condizione = None) -> None:

        super().__init__(descrizione, anni_garanzia, pubblicazione, prezzo, is_nuovo, condizione)
        
        self.setPrezzo_bid(prezzo_bid)
        self.scadenza = scadenza

    # prezzo bid

    def getPrezzo_bid(self) -> RealGZ:
        return self.prezzo_bid

    def setPrezzo_bid(self, prezzo_bid: RealGZ) -> None:
        self.prezzo_bid = prezzo_bid

    # scadenza

    def getScadenza(self) -> date:
        return self.scadenza