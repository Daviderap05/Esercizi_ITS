class Room:
    
    def __init__(self, id: str, floor: int, seats: int):
        
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: int = seats * 2
        
    def get_id(self) -> str:
        
        return self.id

    def get_floor(self) -> int:
        
        return self.floor
    
    def get_seats(self) -> int:
        
        return self.seats
    
    def get_area(self) -> int:
        
        return self.area
    
    
    
class Building:
    
    def __init__(self, name: str, address: str, floors: tuple):
        
        self.name: str = name
        self.address: str = address
        self.floors: tuple = floors
        self.rooms: list[Room] = []
    
    def get_floors(self) -> tuple:
        
        return self.floors 
    
    def get_rooms(self) -> list[Room]:
        
        return self.rooms
    
    def add_room(self, room: Room) -> None:
        
        min_floor, max_floor = self.floors
        
        if min_floor <= room.get_floor() <= max_floor:

            if room not in self.rooms:
                
                self.rooms.append(room)
            
    def area(self) -> int:
        
        area: int = 0
        
        for room in self.rooms:
            
            area += room.get_area()
            
        return area