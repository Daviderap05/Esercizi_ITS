from .car import Car
from .van import Van


class FleetManager:
    def __init__(self, vehicles: dict[str, Car | Van] = None):
        self.vehicles: dict[str, Car | Van] = vehicles if vehicles is not None else {}

    def add(self, vehicle: Car | Van):
        if isinstance(vehicle, (Car, Van)):
            self.vehicles[vehicle.plate_id] = vehicle
            print("Veicolo inserito correttamente")
            return True
        else:
            print ("Veicolo deve essere Van o Car")
            return False

    def get(self, plate_id: str):
        if plate_id in self.vehicles:
            return self.vehicles[plate_id]
        else:
            return None

    def update (self, plate_id: str, new_vehicle: Car | Van):
        if plate_id in self.vehicles and isinstance(new_vehicle, (Car, Van)):
            print("PUT riuscita")
            self.vehicles[plate_id] = new_vehicle
        else:
            print("PUT non riuscita")

    def patch_status (self, plate_id: str, new_status: str):
        if plate_id in self.vehicles and isinstance(new_status, str):
            self.vehicles[plate_id].setStatus(new_status)
            print("PATCH riuscita")
        else:
            print("PATCH non riuscita")

    def delete(self, plate_id: str):
        if plate_id in self.vehicles:
            del self.vehicles[plate_id]
            print("REMOVE riuscita")
            return True
        else:
            print("REMOVE non riuscita")
            return False
        
    def list_all(self):
        return [v.info() for v in self.vehicles.values()] if self.vehicles else []
