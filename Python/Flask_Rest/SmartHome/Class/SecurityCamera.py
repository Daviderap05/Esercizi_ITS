from __future__ import annotations
from dataclasses import dataclass
from Class.SmartDevice import SmartDevice


@dataclass
class SecurityCamera(SmartDevice):
    resolution: str
    night_vision: bool
    power_watt: float | int = 50  # tipico più alto

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        return self.power_watt

    def connection_quality(self) -> int:
        # tipicamente alto (8-10)
        return 9

    def info(self) -> dict[str, float | int | str]:
        data = super().info()
        data.update(
            {
                "resolution": self.resolution,
                "night_vision": self.night_vision,
                "power_watt": self.power_watt,
            }
        )
        return data
