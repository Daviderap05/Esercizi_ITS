from __future__ import annotations  
from movie_genre import *


class Film():
    
    def __init__(self, id: int, title: str) -> None:
        self.setID(id)
        self.setTitle(title)
    
    def setID(self, id: int) -> None:
        if isinstance(id, int) and id >= 0:
            self.__id = id
        else:
            raise ValueError("ID non valido")

            
    def  setTitle(self, title: str) -> None:
        if isinstance(title, str) and title.strip():
            self.__title = title.capitalize()
        else:
            raise ValueError("Titolo non valido")
            
    def getId(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self, otherFilm: Film)  -> bool:
        if not isinstance(otherFilm, Film):
            return False
        return self.__id == otherFilm.getId()