from movie_genre import *

class Noleggio():
    
    def __init__(self, film_list: list[Azione | Commedia | Drama]) -> None:

        self.rented_film: dict[int, list[Azione | Commedia | Drama]] = {}
        
        if isinstance(film_list, list) and all(isinstance(f, (Azione, Commedia, Drama)) for f in film_list):
            self.film_list = film_list
        else:
            raise ValueError ("Errore, inserire una lista di film valida!")
        
        
    def isAvaible(self, film: Azione | Commedia | Drama) -> bool:
        
        if not (isinstance(film, (Azione, Commedia, Drama)) and film):
            raise ValueError ("Errore inserire un film valido!")
        
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return False
    
    
    def rentAMovie(self, film: Azione | Commedia | Drama, clientID: int) -> bool | None:
        
        if not isinstance(clientID, int) or clientID <= 0:
            raise ValueError("Errore: inserire un ID cliente valido.")

        if not self.isAvaible(film):
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")
            return False

        self.film_list.remove(film)
        self.rented_film.setdefault(clientID, []).append(film)
        print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        return True
        
        
    def giveBack(self, film: Azione | Commedia | Drama, clientID: int, days: int) -> None:
        
        if not (
            isinstance(film, (Azione, Commedia, Drama)) and film 
            and isinstance(clientID, int) 
            and isinstance(days, int) and days > 0
        ):
            raise ValueError("Errore, inserire valori validi")
        
        if clientID not in self.rented_film:
            raise ValueError (f"Nessun film noleggiato per il cliente {clientID}.")
        
        if film not in self.rented_film[clientID]:
            raise ValueError ("Errore, l'utente non ha noleggiato questo film.")
        
        self.rented_film[clientID].remove(film)
        self.film_list.append(film)
        
        if not self.rented_film[clientID]:
            del self.rented_film[clientID]
        
        penale: int | float = film.calcolaPenaleRitardo(days)
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {penale} euro!")
        
        
    def printMovies(self) -> None:
        
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()}")
            
            
    def printRentMovies(self, clientID: int) -> None:
        
        if not isinstance(clientID, int) or clientID <= 0:
            raise ValueError("Errore: inserire un ID cliente valido.")
        
        if clientID not in self.rented_film:
            raise ValueError (f"Nessun film noleggiato per il cliente {clientID}.")
        
        for film in self.rented_film[clientID]:
            print(f"{film.getTitle()} - {film.getGenere()}")    