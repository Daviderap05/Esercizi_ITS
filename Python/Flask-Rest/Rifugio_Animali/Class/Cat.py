from .Animal import *


class Cat(Animal):

    def __init__(
        self,
        id: str,
        name: str,
        age_years: int,
        weight_kg: float,
        favorite_toy: str,
        indoor_only: bool,
    ) -> None:
        super().__init__(id, name, age_years, weight_kg)
        self.favorite_toy: str = favorite_toy
        self.indoor_only: bool = indoor_only

    def species(self) -> str:
        return "Cat"

    def daily_food_grams(self) -> float:
        return 100 + self.age_years * 30

    def info(self) -> dict[str, Any]:
        return super().info() | {
            "favorite_toy": self.favorite_toy,
            "indoor_only": self.indoor_only,
        }
