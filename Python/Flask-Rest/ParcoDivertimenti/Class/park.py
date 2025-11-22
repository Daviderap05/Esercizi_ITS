from .ride import Ride

class Park:
    
    def __init__(self, rides: dict[str, Ride] = None) -> None:
        self.rides: dict[str, Ride] = rides if rides is not None else {}
    
    def add(self, ride: Ride) -> None:
        self.rides[ride.id] = ride
        
    def get(self, ride_id: str) -> Ride | None:
        return self.rides.get(ride_id, None)
    
    def list_all(self) -> list[dict[str, str | int]]:
        return [ride.info() for ride in self.rides.values()]