from Class.Animal import *
from Class.Cat import *
from Class.Dog import *
from Class.Shelter import *


shelter: Shelter = Shelter()

shelter.add(
    Dog(
        id="d1",
        name="Buddy",
        age_years=3,
        weight_kg=20.5,
        breed="Labrador",
        is_trained=True,
    )
)
shelter.add(
    Cat(
        id="c1",
        name="Whiskers",
        age_years=2,
        weight_kg=4.3,
        favorite_toy="Mouse",
        indoor_only=False,
    )
)

shelter.set_adopted("d1", "Alice")

print(shelter.list_all())
print(shelter.adoptions)