# isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
from __future__ import annotations  
from movie_genre import *


class Film():
    
    def __init__(self, id: int, title: str) -> None:
        self.setID(id)
        self.setTitle(title)
    
    def setID(self, id: int) -> None:
        if isinstance(id, int) and id:
            self.__id = id
            
    def  setTitle(self, title: str) -> None:
        if isinstance(title, str) and title.strip():
            self.__title = title
            
    def getId(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, otherFilm: Azione | Commedia | Drama):
        return self.__id == otherFilm.getId()
        # usarlo in noleggio (isAvaible)