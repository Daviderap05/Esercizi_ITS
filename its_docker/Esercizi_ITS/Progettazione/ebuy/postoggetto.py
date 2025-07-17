from mytipes import *
from abc import ABC, abstractmethod
from datetime import date
class Postoggetto(ABC):

    _descrizione: str # mutabile, noto alla nascita
    _anni_garanzia: IntGEZ # immutabile ad evoluzione controllata, noto alla nascita
    _pubblicazione: date # immutabile, noto alla nascita
    _prezzo: RealGEZ # immutabile ad evoluzione controllata, noto alla nascita
    _condizione: Condizione # immutabile, probabilmente non noto alla nascita ... [0..1]
    _is_nuovo: bool # immutabile, noto alla nascita 
    
    @abstractmethod
    def __init__(self, *, descrizione: str, anni_garanzia: IntGEZ, pubblicazione: date, prezzo: RealGEZ,\
        is_nuovo: bool, condizione: Condizione = None) -> None:

        self.set_descrizione(descrizione)
        self._anni_garanzia = anni_garanzia
        self._pubblicazione = pubblicazione
        self._prezzo = prezzo
        self._condizione = condizione
        self._is_nuovo = is_nuovo

    # descrizione

    def descrizione(self) -> str:
        return self._descrizione

    def set_descrizione(self, descrizione: str) -> None:
        self._descrizione = descrizione

    # anni_garanzia

    def anni_garanzia(self) -> IntGEZ:
        return self._anni_garanzia

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        # condizione per cui posso ancora modificare gli anni di garanzia
        self._anni_garanzia = anni_garanzia

    # pubblicazione

    def pubblicazione(self) -> date:
        return self._pubblicazione

    # prezzo

    def prezzo(self) -> RealGEZ:
        return self._prezzo

    def set_prezzo(self, prezzo: RealGEZ) -> None:
        # condizione per cui si puo ancora modificare il prezzo
        self._prezzo = prezzo

    # is_nuovo

    def is_nuovo(self) -> bool:
        return self._is_nuovo

    # condizione

    def condizione(self) -> Condizione:
        # se non e valorizzato, rimasto none
        if self._condizione == None:
            print('L \'oggetto e nuovo!')
            return
        return self._condizione



    