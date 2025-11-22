from film import Film


class Azione(Film):
    
    __genere: str = "Azione"
    __penale: float | int = 3
            
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> int | float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, nGiorniRit: int) -> int | float:
        if isinstance(nGiorniRit, int) and nGiorniRit > 0:
            return nGiorniRit * self.getPenale()
        raise ValueError ("Inserire dei giorni di ritardo > 0")
        
      
        
class Commedia(Film):

    __genere: str = "Commedia"
    __penale: float | int = 2.5
    
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> int | float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, nGiorniRit: int) -> int | float:
        if isinstance(nGiorniRit, int) and nGiorniRit > 0:
            return nGiorniRit * self.getPenale()
        raise ValueError ("Inserire dei giorni di ritardo > 0")
        
        

class Drama(Film):

    __genere: str = "Drama"
    __penale: float | int = 2
        
    def __init__(self, id: int, title: str) -> None:
        super().__init__(id, title)
        
    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> int | float:
        return self.__penale
    
    def calcolaPenaleRitardo(self, nGiorniRit: int) -> int | float:
        if isinstance(nGiorniRit, int) and nGiorniRit > 0:
            return nGiorniRit * self.getPenale()
        raise ValueError ("Inserire dei giorni di ritardo > 0")
        