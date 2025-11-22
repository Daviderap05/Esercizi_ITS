from abc import ABC, abstractmethod

class Ride(ABC):
    
    def __init__(self, id: str, name: str, min_height_cm: int) -> None:
        self.id: str = id
        self.name: str = name
        self.min_height_cm: int = min_height_cm
        
    @abstractmethod
    def category(self) -> str:
        pass
    
    @abstractmethod
    def base_wait(self) -> int:
        pass
    
    def info(self) -> dict[str, str | int]:
        return {
            "id": self.id,
            "name": self.name,
            "min_height_cm": self.min_height_cm,
            "category": self.category(),
            "base_wait": self.base_wait()
        }
        
    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return int(self.base_wait() * crowd_factor)