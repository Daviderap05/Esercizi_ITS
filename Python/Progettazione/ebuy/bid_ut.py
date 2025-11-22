from privato import Privato
from bid import Bid
from typing import Any

class bid_ut:

    class _link:

        _privato: Privato # immutabile, noto alla nascita
        _bid: Bid # immutabile, noto alla nascita

        def __init__(self, p: Privato, b: Bid) -> None:

            self._privato = p
            self._bid = b

        def privato(self) -> Privato:
            return self._privato

        def bid(self) -> Bid:
            return self._bid

        def __hash__(self) -> int:
            return ((self.bid(), self.privato()))

        def __eq__(self, other) -> bool:
            if type(other) != type(self) \
                or hash(self) != hash(other):
                return False
            return (self.privato(), self.bid()) == (other.privato(), other.progetto())


    
