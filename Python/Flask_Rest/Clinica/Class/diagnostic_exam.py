from Class.booking import Booking
from typing import Dict, Union


class DiagnosticExam(Booking):
    """
    Rappresenta un esame diagnostico.
    """

    def __init__(
        self,
        booking_id: str,
        patient_name: str,
        doctor: str,
        department: str,
        date: str,
        time: str,
        exam_type: str,
        requires_fasting: bool,
        status: str = "scheduled",
    ):
        super().__init__(
            booking_id, patient_name, doctor, department, date, time, status
        )
        self.exam_type = exam_type
        self.requires_fasting = requires_fasting

    def booking_type(self) -> str:
        return "exam"

    def base_duration(self) -> int:
        return 45  # Durata standard per un esame

    def priority_level(self) -> int:
        # Euristica: RMN/TAC hanno priorità più alta
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn", "mri", "tac", "ct"]:
            return 8
        return 7

    def info(self) -> Dict[str, Union[int, str, bool, float]]:
        data = super().info()
        data["exam_type"] = self.exam_type
        data["requires_fasting"] = self.requires_fasting
        return data
