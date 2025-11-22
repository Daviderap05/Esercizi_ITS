from movie_genre import *

class Noleggio():
    
    def __init__(self, film_list: list[Azione | Commedia | Drama]) -> None:

        self.rented_film: dict[int, list[Azione | Commedia | Drama]] = {}
        
        if isinstance(film_list, list) and all(isinstance(f, (Azione, Commedia, Drama)) for f in film_list):
            self.film_list = film_list
        else:
            raise ValueError ("Errore, inserire una lista di film valida!")
        
        
    def isAvaible(self, film: Azione | Commedia | Drama):
        
        if not (isinstance(film, (Azione, Commedia, Drama)) and film):
            raise ValueError ("Errore inserire un film valido!")
                
        for f in self.film_list:
            if f.isEqual(film):
                print(f"Il film scelto è disponibile: {f.getTitle()}!")
                return f
    
        print(f"Il film scelto non è disponibile: {film.getTitle()}!")
        return None
    
    
    def rentAMovie(self, film: Azione | Commedia | Drama, clientID: int) -> None:
        
        if not isinstance(clientID, int) or clientID <= 0:
            raise ValueError("Errore: inserire un ID cliente valido.")
        
        to_remove: Azione | Commedia | Drama | None  = self.isAvaible(film)

        if to_remove is None:
            return
        
        self.film_list.remove(to_remove)
        self.rented_film.setdefault(clientID, []).append(to_remove)
        print(f"Il cliente {clientID} ha noleggiato {to_remove.getTitle()}!")

        
    def giveBack(self, film: Azione | Commedia | Drama, clientID: int, days: int) -> None:
        
        if not (
            isinstance(film, (Azione, Commedia, Drama)) and film
            and isinstance(clientID, int) and clientID > 0
            and isinstance(days, int) and days > 0
        ):
            raise ValueError("Errore, inserire valori validi")

        if clientID not in self.rented_film or not self.rented_film[clientID]:
            print(f"Nessun film noleggiato per il cliente {clientID}.")

        to_return = None
        for f in self.rented_film[clientID]:
            if f.isEqual(film):
                to_return = f
                break
            
        if to_return == None:
            print(f"Il cliente non ha noleggiato il film: {film.getTitle()}")
                
        self.rented_film[clientID].remove(to_return)
        self.film_list.append(to_return)

        if not self.rented_film[clientID]:
            del self.rented_film[clientID]

        penale = to_return.calcolaPenaleRitardo(days)
        print(f"Cliente: {clientID}! La penale da pagare per il film {to_return.getTitle()} è di {penale} euro!")

        
    def printMovies(self) -> None:
        
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()}")
        
            
    def printRentMovies(self, clientID: int) -> None:
        
        if not isinstance(clientID, int) or clientID <= 0:
            raise ValueError("Errore: inserire un ID cliente valido.")
        
        if clientID not in self.rented_film:
            print(f"Nessun film noleggiato per il cliente {clientID}.")
        
        for film in self.rented_film[clientID]:
            print(f"{film.getTitle()} - {film.getGenere()}")    