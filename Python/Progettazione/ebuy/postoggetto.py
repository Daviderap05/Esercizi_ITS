from mytipes import *
from abc import ABC, abstractmethod
from datetime import date



class Postoggetto(ABC):

    descrizione: str # mutabile, noto alla nascita
    anni_garanzia: IntGEZ # immutabile ad evoluzione controllata, noto alla nascita
    pubblicazione: date # immutabile, noto alla nascita
    prezzo: RealGEZ # immutabile ad evoluzione controllata, noto alla nascita
    condizione: Condizione # immutabile, probabilmente non noto alla nascita ... [0..1]
    is_nuovo: bool # immutabile, noto alla nascita e opzionale
    
    @abstractmethod
    def __init__(self, descrizione: str, anni_garanzia: IntGEZ, pubblicazione: date, prezzo: RealGEZ,\
        is_nuovo: bool, condizione: Condizione = None) -> None:

        self.set_descrizione(descrizione)
        self.anni_garanzia = anni_garanzia
        self.pubblicazione = pubblicazione
        self.prezzo = prezzo
        self.condizione = condizione
        self.is_nuovo = is_nuovo
        
    # descrizione

    def getDescrizione(self) -> str:
        return self.descrizione

    def set_descrizione(self, descrizione: str) -> None:
        self.descrizione = descrizione

    # anni_garanzia

    def getAnni_garanzia(self) -> IntGEZ:
        return self.anni_garanzia

    def set_anni_garanzia(self, anni_garanzia: IntGEZ) -> None:
        # condizione per cui posso ancora modificare gli anni di garanzia
        self.anni_garanzia = anni_garanzia

    # pubblicazione

    def getPubblicazione(self) -> date:
        return self.pubblicazione

    # prezzo

    def getPrezzo(self) -> RealGEZ:
        return self.prezzo

    def set_prezzo(self, prezzo: RealGEZ) -> None:
        # condizione per cui si puo ancora modificare il prezzo
        self.prezzo = prezzo

    # is_nuovo

    def getIs_nuovo(self) -> bool:
        return self.is_nuovo

    # condizione

    def getCondizione(self) -> Condizione:
        # se non e valorizzato, rimane none
        if self.condizione == None:
            return "l'oggetto è nuovo."
        return self.condizione