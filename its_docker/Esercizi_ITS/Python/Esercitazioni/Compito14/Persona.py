class Persona():
    
    def checkAge(self):
        
        if self.__first_name != None and self.__last_name != None:
            self.__eta: int = 0
        else:
            self.__eta: int = None
          
            
    def __init__(self, first_name: str, last_name: str):
        
        if first_name and isinstance(first_name, str): 
            self.__first_name: str = first_name 
        else:
            print("Il nome inserito non è una stringa!")
            self.__first_name: str = None
            
            
        if last_name and isinstance(last_name, str): 
            self.__last_name: str = last_name 
        else:
            print("Il nome inserito non è una stringa!")
            self.__last_name: str = None
                 
                  
        self.checkAge()
            
            
    def setName(self, first_name):
        
        if first_name and isinstance(first_name, str): 
            self.__first_name: str = first_name 
        else:
            print("Il nome inserito non è una stringa!")
            
            
        self.checkAge()
    
    
    def setLastName(self, last_name):
        
        if last_name and isinstance(last_name, str): 
            self.__last_name: str = last_name 
        else:
            print("Il nome inserito non è una stringa!")
            
        
        self.checkAge()
                   
                   
    def setAge(self, age):
        
        if age and isinstance(age, int):
            self.__eta: int = age 
        else: 
            print("L'età deve essere un numero intero!")
        
        
    def getName(self):
        return self.__first_name
    
    
    def getLastname(self):
        return self.__last_name
    
    
    def getAge(self):
        return self.__eta
    
    
    def greet(self):
        
        if isinstance(self.getName(), str) and isinstance(self.getLastname(), str):
            print(f"Ciao, sono {self.getName()} {self.getLastname()}! Ho {self.getAge()} anni!")
            # sistemare con il capitalize
     
     
if __name__ == "__main__":    
    
    persona = Persona(4, 2)
    persona.setName("Davide")
    persona.setLastName("Raponi")
    persona.setAge(19)
    print("")
    persona.greet()