from .ride import Ride

class Carousel(Ride):
    
    def __init__(self, id: str, name: str, min_height_cm: int, animals: list[str] = None) -> None:
        super().__init__(id, name, min_height_cm)
        self.animals: list[str] = animals if animals is not None else []
        
    def category(self) -> str:
        return "Family"
    
    def base_wait(self) -> int:
        return 10
    
    def info(self) -> dict[str, str | int]:
        base_info = super().info()
        base_info["animals"] = self.animals
        return base_info