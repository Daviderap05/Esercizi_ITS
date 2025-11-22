from Persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specializzazione: str, parcella: float | int) -> None:
        super().__init__(first_name, last_name)
        self.__specializzazione: str | None = None
        self.__parcella: float | int | None = None
        self.setSpecializzazione(specializzazione)
        self.setParcella(parcella)

    def setSpecializzazione(self, specializzazione: str) -> None:
        if isinstance(specializzazione, str) and specializzazione.strip():
            self.__specializzazione = specializzazione.strip()
        else:
            print("La specializzazione inserita non è una stringa valida!")
            self.__specializzazione = None

    def setParcella(self, parcella: float | int) -> None:
        if isinstance(parcella, (int, float)) and parcella >= 0:
            self.__parcella = parcella
        else:
            print("La parcella inserita non è un numero valido (>= 0)!")
            self.__parcella = None

    def getSpecializzazione(self) -> str | None:
        return self.__specializzazione

    def getParcella(self) -> float | int | None:
        return self.__parcella

    def isAValidDoctor(self) -> bool:
        eta = self.getAge()
        if isinstance(eta, int) and eta > 30:
            print(f"Il dott. {self.getName()} {self.getLastname()} è valido!")
            return True
        else:
            print(f"Il dott. {self.getName()} {self.getLastname()} non è valido!")
            return False

    def doctorGreet(self) -> None:
        super().greet()
        spec = self.getSpecializzazione() or "senza specializzazione"
        print(f"Sono un medico {spec}")

# if __name__ == "__main__":
#     d1 = Dottore("Davide", "Raponi", "Chirurgo", 19000.0)
#     d1.setAge(49)
#     d1.doctorGreet()
#     d1.isAValidDoctor()