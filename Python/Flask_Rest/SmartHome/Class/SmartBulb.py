from __future__ import annotations
from dataclasses import dataclass
from Class.SmartDevice import SmartDevice


@dataclass
class SmartBulb(SmartDevice):
    brightness_lumens: int
    color_capability: bool
    power_watt: float | int = 9  # tipico 9 o 15

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        return self.power_watt

    def connection_quality(self) -> int:
        # tipicamente basso/medio (2-4)
        return 3

    def info(self) -> dict[str, float | int | str]:
        data = super().info()
        data.update(
            {
                "brightness_lumens": self.brightness_lumens,
                "color_capability": self.color_capability,
                "power_watt": self.power_watt,
            }
        )
        return data
