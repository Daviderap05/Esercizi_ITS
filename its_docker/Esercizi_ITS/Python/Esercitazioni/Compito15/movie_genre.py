from film import Film


class Azione(Film):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        
        self.__genere: str = "Azione"
        self.__penale: float | int = 3
        
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> int | float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, nGiorniRit: int) -> int | float | ValueError:
        if nGiorniRit and nGiorniRit > 0 and isinstance(nGiorniRit, int):
            return nGiorniRit * Azione.getPenale()
        raise ValueError ("Inserire dei giorni di ritardo > 0")
        
      
        
class Commedia(Film):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        
        self.__genere: str = "Commedia"
        self.__penale: float | int = 2.5
        
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> int | float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, nGiorniRit: int) -> int | float | ValueError:
        if nGiorniRit and nGiorniRit > 0 and isinstance(nGiorniRit, int):
            return nGiorniRit * Commedia.getPenale()
        raise ValueError ("Inserire dei giorni di ritardo > 0")
        
        

class Drama(Film):

    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        
        self.__genere: str = "Drama"
        self.__penale: float | int = 2
        
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> int | float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, nGiorniRit: int) -> int | float | ValueError:
        if nGiorniRit and nGiorniRit > 0 and isinstance(nGiorniRit, int):
            return nGiorniRit * Drama.getPenale()
        raise ValueError ("Inserire dei giorni di ritardo > 0")
        