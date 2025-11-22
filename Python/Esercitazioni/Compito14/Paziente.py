from Persona import Persona

class Paziente(Persona):
    
    def __init__(self, first_name: str, last_name: str, idCode: str) -> None:
        super().__init__(first_name, last_name)
        self.__idCode: str | None = None
        self.setIdCode(idCode)
        
    def setIdCode(self, idCode: str) -> None:
        if isinstance(idCode, str) and idCode.strip():
            self.__idCode = idCode.strip()
        else:
            print("Codice ID non valido.")
            self.__idCode = None
        
    def getIdCode(self) -> str | None:
        return self.__idCode
    
    def patientInfo(self) -> None:
        nome = self.getName()
        cognome = self.getLastname()
        codice = self.getIdCode() or "N/D"
        print(f"Paziente: {nome} {cognome}\nID: {codice}")


# if __name__ == "__main__":
#     paz = Paziente("Davide", "Raponi", "fgndmh")
#     paz.patientInfo()