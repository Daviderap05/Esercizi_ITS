from Class.booking import Booking
from typing import Dict, Union


class MedicalVisit(Booking):
    """
    Rappresenta una visita medica.
    """

    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        visit_reason: str,
        first_time: bool,
        status: str = "scheduled",
    ):
        super().__init__(
            booking_id, patient_name, doctor, department, date, time, status
        )
        self.visit_reason = visit_reason
        self.first_time = first_time

    def booking_type(self) -> str:
        return "visit"

    def base_duration(self) -> int:
        return 30  # Durata standard per una visita

    def priority_level(self) -> int:
        # Euristica basata su parole chiave
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]
        for k in keywords:
            if k in reason:
                return 7
        return 5

    def info(self) -> Dict[str, Union[int, str, bool, float]]:
        # Ottiene le info base e aggiunge quelle specifiche
        data = super().info()
        data["visit_reason"] = self.visit_reason
        data["first_time"] = self.first_time
        return data
