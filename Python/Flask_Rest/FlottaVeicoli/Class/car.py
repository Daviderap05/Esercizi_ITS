from .veichle import *
from typing import Any

class Car(Veichle):
    def __init__(
        self,
        plate_id: str,
        model: str,
        registration_year: str,
        status: str = "available",
        driver_name: str = None,
        doors: int = 5,
        is_cabrio: bool = False,
    ):
        super().__init__(plate_id, model, registration_year, status, driver_name)
        self.setDoors(doors)
        self.setIsCabrio(is_cabrio)

    def setDoors(self, doors: int):
        if isinstance(doors, int) and doors in (3, 5):
            print(f"Macchina con {doors} porte.")
            self.doors = doors
        else:
            raise ValueError("Porte impossibili.")

    def setIsCabrio(self, is_cabrio: bool):
        if is_cabrio:
            print("Macchina cabrio")
            self.is_cabrio = True
        elif not is_cabrio:
            print("Macchina non cabrio")
            self.is_cabrio = False
        else:
            raise ValueError("Indefinito")

    def vehicle_type(self):
        return "Car"

    def base_cleaning_time(self):
        # restituisce il tempo base di pulizia del veicolo in minuti
        return 30

    def wear_level(self):
        # restituisce un intero che rappresenta il livello di usura medio del veicolo
        return 1                                

    def info(self):
        d: dict[str, Any] = super().info()
        d.update({"doors": self.doors, "is_cabrio": self.is_cabrio})
        return d
