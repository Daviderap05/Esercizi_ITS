from abc import ABC, abstractmethod
from typing import Any


class Animal(ABC):
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id: str = id
        self.name: str = name
        self.age_years: int = age_years
        self.weight_kg: float = weight_kg
        
    @abstractmethod
    def species(self) -> str:
        pass
    
    @abstractmethod
    def daily_food_grams(self) -> float:
        pass
    
    def info(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "age_years": self.age_years,
            "weight_kg": self.weight_kg,
            "species": self.species(),
            "daily_food_grams": self.daily_food_grams()
        }
        
    def bmi_like(self) -> float:
        return self.weight_kg / (self.age_years + 1)