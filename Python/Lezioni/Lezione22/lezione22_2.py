class Media():
    
    def __init__(self, title: str, reviews: list[int] = None) -> None:
        
        self.set_title(title)
        
        # metodo migliore per gestire liste vuote iniziali nel costruttore
        self.reviews: list[int] = reviews if reviews is not None else []
        
        
    def set_title(self, title: str) -> None:
        
        if title and isinstance(title, str):
            self.title: str = title
            
            
    def get_title(self) -> str:
        
        return self.title
    
    
    def aggiungiValutazione(self, voto: int) -> None:
        
        if voto and isinstance(voto, int) and 1 <= voto <= 5:
            self.reviews.append(voto)
        else:
            raise ValueError ("Errore... voto non valido, deve essere un intero compreso tra 1 e 5")
        
        
    def getMedia(self) -> float:
        
        if len(self.reviews) > 0:
            return sum(self.reviews) / len(self.reviews)
        
        raise ValueError ("Errore... Non sono presenti voti")
    
    
    def getRate(self) -> str:

        match round(self.getMedia()):
            
            case 1: 
                return "Terribile"
            
            case 2:
                return "Brutto"
            
            case 3: 
                return "Normale"
            
            case 4:
                return "Bello"
            
            case 5: 
                return "Grandioso"
            
            case _:
                return f"Errore nel calcolo dell'arrotondamento"
            
    
    def ratePercentage(self, voto: int) -> float:
        
        if isinstance(voto, int) and 1 <= voto <= 5:
            
            if len(self.reviews) == 0:
                return 0.0
            
            return (self.reviews.count(voto) / len(self.reviews)) * 100
        
        else:
            
            raise ValueError("Errore... voto non valido, deve essere un intero compreso tra 1 e 5")

        
    def recensione(self) -> None:    
    
        print(f"Titolo del film: {self.get_title()}")
        print(f"Voto Medio: {self.getMedia()}")
        print(f"Giudizio: {self.getRate()}")
        print(f"Terribile: {self.ratePercentage(1):.2f}%")
        print(f"Brutto: {self.ratePercentage(2):.2f}%")
        print(f"Normale: {self.ratePercentage(3):.2f}%")
        print(f"Bello: {self.ratePercentage(4):.2f}%")
        print(f"Grandioso: {self.ratePercentage(5):.2f}%\n")

        
    
class Film(Media):
    
    def __init__(self, title: str, reviews: list[int] = None) -> None:
        super().__init__(title, reviews)
        
        
    def set_title(self, title: str):
        return super().set_title(title)
    
    

film1: Film = Film("The Shawshank Redemption")
film2: Film = Film("Alien")

for voto in [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]:
    
    film1.aggiungiValutazione(voto)
    film2.aggiungiValutazione(voto)
    
film1.recensione()
film2.recensione()