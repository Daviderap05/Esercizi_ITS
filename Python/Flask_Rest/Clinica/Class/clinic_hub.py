from typing import Dict, List, Optional, Union
from Class.booking import Booking


class ClinicHub:
    """
    Gestisce il sistema delle prenotazioni.
    """

    def __init__(self):
        # Dizionario: booking_id -> Oggetto Booking
        self.bookings: Dict[str, Booking] = {}

    def add(self, booking: Booking) -> bool:
        """Aggiunge una prenotazione. False se ID già presente."""
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True

    def get(self, booking_id: str) -> Optional[Booking]:
        """Restituisce la prenotazione o None."""
        return self.bookings.get(booking_id)

    def update(self, booking_id: str, new_booking: Booking) -> None:
        """Sostituisce completamente una prenotazione esistente."""
        if booking_id in self.bookings:
            self.bookings[booking_id] = new_booking

    def patch_status(self, booking_id: str, new_status: str) -> None:
        """Aggiorna solo lo stato di una prenotazione."""
        booking = self.get(booking_id)
        if booking:
            booking.status = new_status

    def delete(self, booking_id: str) -> bool:
        """Rimuove la prenotazione. True se successo."""
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return True
        return False

    def list_all(self) -> List[Dict[str, Union[int, str, bool, float]]]:
        """Restituisce una lista di dizionari con le info di tutte le prenotazioni."""
        return [b.info() for b in self.bookings.values()]
