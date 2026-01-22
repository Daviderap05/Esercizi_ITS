from Class.IoTHub import IoTHub
from Class.SmartBulb import SmartBulb
from Class.SecurityCamera import SecurityCamera

hub = IoTHub()

hub.add(
    SmartBulb(
        serial_number="SN-101",
        brand="Philips Hue",
        room="Living Room",
        installation_year=2023,
        status="online",
        brightness_lumens=800,
        color_capability=True,
        power_watt=9,
    )
)

hub.add(
    SecurityCamera(
        serial_number="SN-10293-X",
        brand="Nest",
        room="Entrance",
        installation_year=2022,
        status="online",
        resolution="1080p",
        night_vision=True,
        power_watt=50,
    )
)
