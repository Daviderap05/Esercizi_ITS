from abc import ABC, abstractmethod
from typing import Dict, Union


class Booking(ABC):
    """
    Classe astratta che rappresenta una generica prenotazione.
    """

    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        status: str = "scheduled",
    ):
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    # --- Metodi Astratti ---
    @abstractmethod
    def booking_type(self) -> str:
        """Restituisce il tipo di prenotazione (es. 'visit', 'exam')."""
        pass

    @abstractmethod
    def base_duration(self) -> int:
        """Restituisce la durata standard della prenotazione in minuti."""
        pass

    @abstractmethod
    def priority_level(self) -> int:
        """Restituisce un indicatore di priorità (1-10)."""
        pass

    # --- Metodi Concreti ---
    def info(self) -> Dict[str, Union[int, str, bool, float]]:
        """Restituisce un dizionario con le informazioni principali."""
        return {
            "booking_id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "type": self.booking_type(),
        }

    def estimated_wait(self, factor: float = 1.0) -> int:
        """
        Calcola l’attesa stimata in minuti.
        Formula: base_duration() * factor + priority_level() * 5
        """
        wait_time = (self.base_duration() * factor) + (self.priority_level() * 5)
        return int(wait_time)
