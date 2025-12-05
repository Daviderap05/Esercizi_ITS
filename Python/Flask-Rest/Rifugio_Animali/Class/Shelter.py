from .Animal import *
from .Cat import *
from .Dog import *


class Shelter:
    def __init__(
        self,
        animals: dict[str, Animal | Cat | Dog] | None = None,
        adoptions: dict[str, str] | None = None,
    ) -> None:
        if animals is None:
            animals = {}

        if adoptions is None:
            adoptions = {}

        self.animals: dict[str, Animal | Cat | Dog] | None = animals
        self.adoptions: dict[str, str] | None = adoptions

    # sovrascrive l'animale se esiste già
    def add(self, animal: Animal | Cat | Dog) -> None:
        self.animals[animal.id] = animal

    def get(self, animal_id: str) -> Animal | Cat | Dog | None:
        if animal_id not in self.animals:
            return None
        return self.animals[animal_id]

    def list_all(self) -> list[dict[str, Any]]:
        return [animal.info() for animal in self.animals.values()]

    def is_adoptded(self, animal_id: str) -> bool:
        return True if animal_id in self.adoptions else False

    def set_adopted(self, animal_id: str, adopter_name: str) -> bool:
        if animal_id not in self.animals:
            return False

        self.adoptions[animal_id] = adopter_name
        return True