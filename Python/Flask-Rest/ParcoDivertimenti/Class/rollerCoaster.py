from .ride import Ride

class RollerCoaster(Ride):
    
    def __init__(self, id: str, name: str, min_height_cm: int, inversions: int) -> None:
        super().__init__(id, name, min_height_cm)
        self.setInversions(inversions)
        
    def setInversions(self, inversions: int) -> None:
        if isinstance(inversions, int) and inversions >= 1:
            self.inversions: int = inversions
        else:
            print("Invalid number of inversions. Please enter an integer greater than or equal to 1.\n\n")
        
    def category(self) -> str:
        return "Roller Coaster"
    
    def base_wait(self) -> int:
        return 40
    
    def info(self) -> dict[str, str | int]:
        base_info: dict[str, str | int] = super().info()
        base_info["inversions"] = self.inversions
        return base_info