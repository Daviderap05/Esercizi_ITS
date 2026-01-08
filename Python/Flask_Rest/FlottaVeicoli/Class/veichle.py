from abc import ABC, abstractmethod
import re


class Veichle(ABC):

    def __init__(
        self,
        plate_id: str,
        model: str,
        registration_year: int,
        status: str = "available",
        driver_name: str = None,
    ):
        self.setTarga(plate_id)
        self.setNome(driver_name)
        self.setRegistrazione(registration_year)
        self.setModel(model)
        self.setStatus(status)

    def setTarga(self, plate_id: str):
        regex: str = r"^[A-Z]{2}\s?\d{3}\s?[A-Z]{2}$"

        if re.match(regex, plate_id):
            print(f"'{plate_id}' è una targa standard valida.")
            self.plate_id = plate_id
        else:
            raise ValueError(f"'{plate_id}' non è una targa standard valida.")

    def setNome(self, driver_name: str):
        if isinstance(driver_name, str) and driver_name.isalpha() and driver_name:
            print(f"'{driver_name}' è diventato proprietario del veicolo")
            self.driver_name = driver_name
        else:
            self.driver_name = None
            print("Errore, nome non valido. Impostato di default a None.")

    def setRegistrazione(self, registration_year: int):
        if (
            isinstance(registration_year, int)
            and len(str(registration_year).strip()) == 4
        ):
            print(f" anno di registrazione: '{registration_year}'")
            self.registration_year = registration_year
        else:
            raise ValueError(f"'{registration_year}' non è un anno valido.")

    def setModel(self, model: str):
        if isinstance(model, str) and model:
            print(f" modello inserito correttamente: '{model}'")
            self.model = model
        else:
            raise ValueError(f"'{model}' non è un modello valido.")

    def setStatus(self, status: str):
        lista: list[str] = ["available", "rented", "maintenance", "cleaning", "retired"]

        if status.lower().strip() in lista:
            print(f" stato modificato: '{status}'")
            self.status = status
        else:
            raise ValueError(f"'{status}' non è uno stato valido.")

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def base_cleaning_time(self):
        pass

    @abstractmethod
    def wear_level(self):
        pass

    def info(self):
        return {
            "id": self.plate_id,
            "model": self.model,
            "driver_name": self.driver_name,
            "veichle_type": self.vehicle_type(),
            "registration_year": self.registration_year,
            "status": self.status,
            # più eventuali campi specifici delle sottoclassi
        }

    def estimated_prep_time(self, factor: float = 1.0):
        return f" tempo di preparazione stimato: {self.base_cleaning_time() * factor + self.wear_level() * 15} minuti"
