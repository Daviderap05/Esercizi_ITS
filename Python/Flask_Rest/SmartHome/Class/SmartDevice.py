from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SmartDevice(ABC):
    serial_number: str
    brand: str
    room: str
    installation_year: int
    status: str  # es: "online", "offline", "updating", "error"

    @abstractmethod
    def device_type(self) -> str:
        pass

    @abstractmethod
    def energy_consumption(self) -> float | int:
        pass

    @abstractmethod
    def connection_quality(self) -> int:
        pass

    def info(self) -> dict[str, float | int | str]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "type": self.device_type(),
        }

    def diagnostics_time(self, factor: float = 1.0) -> float:
        # formula: energy_consumption() * factor + connection_quality()*10
        return self.energy_consumption() * factor + self.connection_quality() * 10
