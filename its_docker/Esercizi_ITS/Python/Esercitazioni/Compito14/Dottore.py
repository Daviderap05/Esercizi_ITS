from Persona import Persona


class Dottore(Persona):
    
    def __init__(self, first_name: str, last_name: str, specializzazione: str, parcella: float):
        
        super().__init__(first_name, last_name)
        
        if specializzazione and isinstance(specializzazione, str):
            self.__specializzazione = specializzazione
        else:
            print("La specializzazione inserita non è una stringa!")
            self.__specializzazione = None
            
        if parcella and isinstance(parcella, float):
            self.__parcella = parcella
        else:
            print("La parcella inserita non è un float!")
            self.__parcella = None
            
            
    def setSpecializzazione(self, specializzazione: str):
        
        if specializzazione and isinstance(specializzazione, str):
            self.__specializzazione = specializzazione
        else:
            print("La specializzazione inserita non è una stringa!")
            
    
    def setParcella(self, parcella):
        
        if parcella and isinstance(parcella, float):
            self.__parcella = parcella
        else:
            print("La parcella inserita non è un float!")
            
    
    def getSpecializzazione(self):
        return self.__specializzazione
    
    
    def getParcel(self):
        return self.__parcella
    
    
    def isAValidDoctor(self):
        
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} e {self.getLastname()} is valid!")
        else:
            print(f"Doctor {self.getName()} e {self.getLastname()} is not valid!")
            
            
    def doctorGreet(self):
        
        super().greet()
        print(f"Sono un medico {self.getSpecializzazione()}")



if __name__ == "__main__":

    print("")
    d1 = Dottore("Davide", "Raponi", "Chirurgo", 19000.0)
    d1.setAge(49)
    d1.doctorGreet()
    d1.isAValidDoctor()