from .veichle import *


class Van(Veichle):

    def __init__(
        self,
        plate_id: str,
        model: str,
        registration_year: str,
        max_load_kg: int,
        status: str = "available",
        driver_name: str = None,
        require_special_license: bool = False,
    ):
        super().__init__(plate_id, model, registration_year, status, driver_name)
        self.setMaxLoadKg(max_load_kg)
        self.setRequire_special_license()

    def setMaxLoadKg(self, max_load_kg: int):
        if isinstance(max_load_kg, int):
            print(f"Portata massima del veicolo impostata a: {max_load_kg}")
            self.max_load_kg = max_load_kg
        else:
            raise ValueError("Errore valore impossibile")

    # mi calcolo la necessità della patente C da max_load_kg
    def setRequire_special_license(self):
        if self.max_load_kg > 3500:
            print("Patente C necessaria")
            self.require_special_license = True
        elif self.max_load_kg <= 3500:
            print("Patente C non necessaria")
            self.require_special_license = False

    def vehicle_type(self):
        return "Van"

    def base_cleaning_time(self):
        # restituisce il tempo base di pulizia del veicolo in minuti
        return 60

    def wear_level(self):
        # restituisce un intero che rappresenta il livello di usura medio del veicolo
        return 4

    def info(self):
        d = super().info()
        d.update(
            {
                "max_load_kg": self.max_load_kg,
                "require_special_license": self.require_special_license,
            }
        )
        return d
