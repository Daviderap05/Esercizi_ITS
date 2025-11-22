class Movie:
    
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False) -> None:
        
        self.movie_id: str = movie_id
        self.title: str = title
        self.director: str = director
        self.is_rented: bool = is_rented
        
    
    def rent(self) -> str|None:
        
        if not self.is_rented:
            
            self.is_rented = True
            
        else:
            
            return f"Il film '{self.title}' è già noleggiato."
        
        
    def return_movie(self) -> str|None:
        
        if self.is_rented:
            
            self.is_rented = False
            
        else:
            
            return f"Il film '{self.title}' non è stato noleggiato da questo cliente."
        
        
        
class Customer():
    
    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = []) -> None:
        
        self.customer_id: str = customer_id
        self.name: str = name
        self.rented_movies: list[Movie] = rented_movies
        
    def rent_movie(self, movie: Movie) -> str|None:
        
        if movie.is_rented == False:
            
            self.rented_movies.append(movie)
            
        else:
            
            return f"Il film '{movie.title}' è già noleggiato."
        
        
    def return_movie(self, movie: Movie) -> str|None:
        
        if movie in self.rented_movies:
            
            self.rented_movies.remove(movie)
            
        else:
            
            return f"Il film '{movie.title}' non è stato noleggiato da questo cliente."
        
        
        
class VideoRentalStore():
    
    def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer]) -> None:
        
        self.movies: dict[str, Movie] = movies
        self.customers: dict[str, Customer] = customers
        
        
    def add_movie(self, movie_id: str, title: str, director: str) -> str|None:
        
        if movie_id in self.movies:
            
            return f"Il film con ID '{movie_id}' esiste già."
        
        movie: Movie = Movie(movie_id, title, director)
        self.movies[movie_id] = movie
        
        
    def register_customer(self, customer_id: str, name: str) -> str|None:
        
        if customer_id in self.customers:
            
            return f"Il cliente con ID '{customer_id}' è già registrato."
        
        customer: Customer = Customer(customer_id, name)
        self.customers[customer_id] = customer
        
        
    def rent_movie(self, customer_id: str, movie_id: str) -> str|None:
        
        if not(customer_id in self.customers and movie_id in self.movies):
            
            return "Cliente o film non trovato."
        
        self.movies[movie_id].rent()
        self.customers[customer_id].rent_movie(self.movies[movie_id])
        
        
    def return_movie(self, customer_id: str, movie_id: str) -> str|None:
        
        if not(customer_id in self.customers and movie_id in self.movies):
            
            return "Cliente o film non trovato."
        
        self.movies[movie_id].return_movie()
        self.customers[customer_id].return_movie(self.movies[movie_id])
        
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        
        if not customer_id in self.customers:
            
            print("Cliente non trovato.")
            return []
        
        return self.customers[customer_id].rented_movies