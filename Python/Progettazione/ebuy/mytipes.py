from typing import Self
from enum import StrEnum, auto
import re 

class Voto(int):

    def __new__(cls, v: int) -> Self:
        if v >= 0 and v <= 5:
            return super().__new__(cls, v)

        raise ValueError('Il voto deve essere un numero tra 0 e 5')

class IntGEZ(int):

    def __new__(cls, n: int) -> Self:
        if n >= 0:
            return super().__new__(cls, n)
        
        raise ValueError('Il numero deve essere maggiore o uguale a zero')

class RealGEZ(float):

    def __new__(cls, n: float) -> Self:
        if n >= 0:
            return super().__new__(cls, n)
        
        raise ValueError('Il numerod deve essere maggiore o uguale a zero')

class Condizione(StrEnum):

    ottimo = auto()
    buono = auto()
    discreto = auto()
    da_sistemare = auto()

class RealGZ(float):

    def __new__(cls, n: float) -> Self:
        if n > 0:
            return super().__new__(cls, n)

        raise ValueError('IL numero deve essere maggiore di zero')

class RealZO(float):

    def __new__(cls, n: float) -> Self:
        if n >= 0 and n <= 1:
            return super().__new__(cls, n)

        raise ValueError('Il numero deve essere compreso tra 0 e 1')

class Popolarita(StrEnum):

    bassa = auto()
    media = auto()
    alta = auto()

class URL(str):

    def __new__(cls, url: str) -> Self:
        pattern = r'^https?://[^\s]+$'

        if re.match(pattern, url):
            return super().__new__(cls, url)

        raise ValueError('Inserire un URL corretto')
