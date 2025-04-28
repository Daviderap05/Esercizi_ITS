class Alieno:
    
    #inizializzazione della classe alieno
    
    def __init__(self, galaxy: str):
        
        self.setGalaxy(galaxy)
        
    def setGalaxy(self, galaxy: str) -> None:   
        
        if galaxy:
            
            self.galaxy = galaxy
            
        else:
            
            print("Errre la galassia non può essere una stringa vuota")
            
    def getGalaxy(self) -> str:
    
        return self.galaxy 
    
    def speak(self) -> str:
        
        print("xfgnfghjdg")
        
    def __str__(self) -> str:
        
        return f"Alieno proveniente dalla galassia {self.getGalaxy()}"