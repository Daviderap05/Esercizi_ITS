#importazione librerie per usare le regex e per restituire più di un tipo in una funzione
import re
from typing import Union

class MovieCatalog:
    
    '''
    
    Attributi della classe:
    self.catalog: dict[str, list[str]]
    
    '''
    
    #inizializzare un oggetto della classe
    def __init__(self) -> None:
        
        self.setCatalog()
    
    #metodi __str__
    
    def __str__(self):
        
        string: str = ""
        
        for key, value in self.catalog.items():
            
            string = "\n" + key + ": " + str(value) + "\n"
            
        return string
    
    #metodi setter
    
    #metodo che imposta il valore dell'attributo self.catalog
    def setCatalog(self) -> None:
        
        self.catalog: dict[str, list[str]] = {}
    

    #metodi getter
    
    #un metodo che ritorna un valore dell'attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:
        
        return self.catalog
    
    #metodi della classe
    
    #metodo che aggiunge una lista di film al catalogo
    def add_movie(self, director_name: str, movies: list[str]) -> None:
        
        #check valore valido di director_name 
        if not director_name:
            
            print("Fornire un nome valido per il regista")
            
        #check valore valido di movies
        elif not movies:
            
            print("Fornire una lista di film che non sia vuota")
            
        #se i dati inseriti sono validi
        else:
            
            #se il regista è presente nel catalogo, aggiungi i film
            if director_name in self.catalog:
                
                #aggiungere film al catalogo
                for movie in movies:
                    
                    #controlliamo se i film della lista movies siano già inseriti dentro il catalogo
                    #dizionario[key] -> ritorna il valore corrispondente alla chiave key
                    #self.catalog[director_name] è la lista di film prodotti dal regista director_name
                    #dove self.catalog è un dizionario 
                    #dove director_name è la chiave
                    #self.catalog[director_name] è il valore corrispondente alla chiave director_name
                    if movie in self.catalog[director_name]:    
                        
                        print(f"il film {movie} è già presente nel catalogo")
                    
                    #un film della lista movies non è già presente nel catalogo    
                    else:
                        
                        self.catalog[director_name].append(movie)
            
            #se il regista non è presente nel catalogo, creare un nuovo record           
            #che ha come chiave il nome del regista e come valore la lista di film
            else:
                
                self.catalog[director_name] = movies
           
                
    #metodo che rimuove un film dal catalogo
    def remove_movie(self, director_name: str, movie: str) -> None:
    
        #check valore valido di director_name 
        if not director_name:
            
            print("Fornire un nome valido per il regista")
            
        #check valore valido di movies
        elif not movie:
            
            print("Fornire un film valido")
            
        #se i dati inseriti sono validi
        else:
            
            #se il regista è presente nel catalogo, e check se il film da rimuovere 
            #è presente nella lista dei film prodotti dal regista rimuoviamo il film
            if director_name in self.catalog and movie in self.catalog[director_name]:
                
                #rimuovere il film dalla lista
                self.catalog[director_name].remove(movie)
            
            #se la lista di film è vuota, rimuovi il regista dal catalogo
            if not self.catalog[director_name]:
                
                #rimuoviamo il regista dal catalogo
                del self.catalog[director_name]
                 
                      
    #metodo per visualizzare una lista di registi del catalogo
    def list_director(self) -> list[str]:
        
        return list(self.catalog.keys())
    
    
    #metodo per troare tutti i film di un regista specifico
    def get_movies_by_director(self, director_name: str) -> None:
        
        #check valore valido di director_name 
        if not director_name:
            
            print("Fornire un nome valido per il regista")
            
        #se i dati inseriti sono validi
        else:
            
            #se il regista è presente nel catalogo
            if director_name in self.catalog:
                
                print(f"Film del regista {director_name}: {self.catalog[director_name]}")
            
            #se il regista non è presente nel catalogo    
            else:
                
                print("Regista sconosciuto")
              
                
    #metodo per trovare tutti i film che contengono una certa parola nel titolo  
    def search_movies_by_title(self, title: str) -> Union[list[tuple[str, str]], str]:
        
        #controlla se il titolo fornito è valido
        if not title:
            
            #se il titolo è vuoto o None, restituisce un messaggio di errore
            return "Fornire un titolo valido per la ricerca"
        
        #se i dati inseriti sono validi
        else:    
            
            #inizializza una lista per memorizzare i risultati della ricerca
            result: list[str] = []
             
            #itera su tutti i registi e i loro film nel catalogo
            for director, movies in self.catalog.items():
                
                #itera su ogni film della lista di film del regista
                for movie in movies:
                    
                    #utilizza una regex per verificare se il titolo cercato è presente nel nome del film
                    if (re.search(title, movie, re.IGNORECASE)):
                        
                        #se il titolo corrisponde, aggiunge una tupla (regista, film) alla lista dei risultati
                        result.append((director, movie))
                    
            #se ci sono risultati, li restituisce
            if result:
                
                return result
            
            #se non ci sono risultati, restituisce un messaggio di errore
            else:
                
                return "Nessun film trovato con la parola cercata"