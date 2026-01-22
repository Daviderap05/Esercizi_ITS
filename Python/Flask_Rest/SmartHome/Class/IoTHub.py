from __future__ import annotations
from typing import Optional
from Class.SmartDevice import SmartDevice


class IoTHub:
    def __init__(self) -> None:
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number in self.devices:
            return False
        self.devices[device.serial_number] = device
        return True

    def get(self, serial_number: str) -> Optional[SmartDevice]:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        # sostituzione completa (simula PUT)
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        # aggiornamento parziale (simula PATCH)
        device = self.get(serial_number)
        if device is None:
            raise KeyError(f"Device '{serial_number}' not found")
        device.status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number not in self.devices:
            return False
        del self.devices[serial_number]
        return True

    def list_all(self) -> list[dict[str, float | int | str]]:
        return [d.info() for d in self.devices.values()]
