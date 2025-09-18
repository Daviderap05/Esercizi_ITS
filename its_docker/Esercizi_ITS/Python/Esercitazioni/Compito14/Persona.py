class Persona:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.__first_name: str | None = None
        self.__last_name: str | None = None
        self.__eta: int | None = None

        self.setName(first_name)
        self.setLastName(last_name)

        if self.__first_name is not None and self.__last_name is not None:
            self.__eta = 0
        else:
            self.__eta = None

    def setName(self, first_name) -> None:
        if isinstance(first_name, str) and first_name.strip():
            self.__first_name = first_name.strip()
            if self.__eta is None and self.__last_name is not None:
                self.__eta = 0
        else:
            print("Il nome inserito non è una stringa valida!")
            self.__first_name = None
            self.__eta = None

    def setLastName(self, last_name) -> None:
        if isinstance(last_name, str) and last_name.strip():
            self.__last_name = last_name.strip()
            if self.__eta is None and self.__first_name is not None:
                self.__eta = 0
        else:
            print("Il cognome inserito non è una stringa valida!")
            self.__last_name = None
            self.__eta = None

    def setAge(self, age) -> None:
        if isinstance(age, int) and age >= 0:
            self.__eta = age
        else:
            print("L'età deve essere un numero intero >= 0!")

    def getName(self) -> str | None:
        return self.__first_name

    def getLastname(self) -> str | None:
        return self.__last_name

    def getAge(self) -> int | None:
        return self.__eta

    def greet(self) -> None:
        nome = self.getName()
        cognome = self.getLastname()
        eta = self.getAge()

        if isinstance(nome, str) and isinstance(cognome, str):
            if isinstance(eta, int):
                print(f"Ciao, sono {nome.capitalize()} {cognome.capitalize()}! Ho {eta} anni!")
            else:
                print(f"Ciao, sono {nome.capitalize()} {cognome.capitalize()}!")
        else:
            print("Ciao! (dati anagrafici incompleti)")
     
     
# if __name__ == "__main__":    
    
#     persona = Persona(4, 2)
#     persona.setName("Davide")
#     persona.setLastName("Raponi")
#     persona.setAge(19)
#     print("")
#     persona.greet()