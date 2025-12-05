from .Animal import *


class Dog(Animal):

    def __init__(
        self,
        id: str,
        name: str,
        age_years: int,
        weight_kg: float,
        breed: str,
        is_trained: bool,
    ) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.breed: str = breed
        self.is_trained: bool = is_trained

    def species(self) -> str:
        return "Dog"

    def daily_food_grams(self) -> float:
        return 200 + self.age_years * 50

    def info(self) -> dict[str, Any]:
        return super().info() | {
            "breed": self.breed,
            "is_trained": self.is_trained,
        }
