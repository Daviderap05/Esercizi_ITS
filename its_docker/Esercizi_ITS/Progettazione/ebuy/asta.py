from postoggetto import Postoggetto
from mytipes import *
from datetime import date
from bid import Bid
from asta_bid import asta_bid

class Asta(Postoggetto):

    _prezzo_bid: RealGZ # mutabile, noto alla nascita
    _scadenza: date # immutabile, noto alla nascita
    _bid_ricevuti: dict[Bid, asta_bid._link] # immutabile, probabilmente non noto alla nascita

    def __init__(self, descrizione: str, anni_garanzia: IntGEZ, pubblicazione: date, prezzo: RealGEZ, is_nuovo: bool,\
        prezzo_bid: RealGZ, scadenza: date, condizione: Condizione = None) -> None:

        super().__init__(descrizione=descrizione, anni_garanzia=anni_garanzia, pubblicazione=pubblicazione, prezzo=prezzo, is_nuovo=is_nuovo,\
            condizione=Condizione)
        
        self.set_prezzo_bid(prezzo_bid)
        self._scadenza = scadenza

    # prezzo bid

    def prezzo_bid(self) -> RealGZ:
        return self._prezzo_bid

    def set_prezzo_bid(self, prezzo_bid: RealGZ) -> None:
        self._prezzo_bid = prezzo_bid

    # scadenza

    def scadenza(self) -> date:
        return self._scadenza

    def add_link_asta_bid(self, l: asta_bid._link) -> None:
        if l.asta() is not self:
            raise ValueError('Il link non mi coinvolge')

        if l.bid in self._bid_ricevuti:
            raise KeyError('Il link gia esiste')

        self._bid_ricevuti[l.bid()] = l

