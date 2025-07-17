from datetime import date
from privato import Privato
from bid_ut import bid_ut
from mytipes import *
from asta import Asta
from asta_bid import asta_bid

class Bid:

    _istante: date # immutabile, noto alla nascita
    _privato: bid_ut._link.privato() # immutabile, da link associ. bid_ut [1..1]
    _asta: asta_bid._link
    

    def __init__(self, istante: date, privato: bid_ut._link, asta: asta_bid._link) -> None:
        self._istante = istante
        self.add_link_bid_ut(privato)
        self.add_link_asta_bid(asta)

    def istante(self) -> date:
        return self._istante

    def add_link_bid_ut(self, l: bid_ut._link) -> None:
        if l.bid() is not self:
            raise ValueError('Il link non mi coinvolge')

        self._privato = l.privato()

    def add_link_asta_bid(self, l: asta_bid._link) -> None:
        if l.bid() is not self:
            raise ValueError('Il link non mi coinvolge')

        self._asta = l.asta()


    