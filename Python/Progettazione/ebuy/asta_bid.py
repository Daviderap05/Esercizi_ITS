from mytipes import *
from asta import Asta
from bid import Bid
from typing import Any

class asta_bid:

    class _link:
        
        _asta: Asta # immutabile, noto alla nascita
        _bid: Bid # immutabile noto alla nascita

        def __init__(self, a: Asta, b: Bid) -> None:
            self._asta = a
            self._bid = b
        
        def asta(self) -> Asta:
            return self._asta

        def bid(self) -> Bid:
            return self._bid

        def __hash__(self) -> int:
            return ( (self.asta(), self.bid()) )

        def __eq__(self, other: Any) -> bool:
            if type(other) != type(self) \
                or hash(self) != hash(other):
                return False
            return (self.asta(), self.bid()) == (other.asta(), other.bid())

