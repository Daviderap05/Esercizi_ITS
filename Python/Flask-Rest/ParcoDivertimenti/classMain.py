from Class.park import Park
from Class.rollerCoaster import RollerCoaster
from Class.carousel import Carousel


     
park: Park = Park()

park.add(RollerCoaster(id="rc1", name="Thunderbolt", min_height_cm=120, inversions=3))
park.add(Carousel(id="c1", name="Merry-Go-Round", min_height_cm=0, animals=["Horse", "Lion", "Elephant"]))

park.add(RollerCoaster(id="rc2", name="Cyclone", min_height_cm=130, inversions=2))
park.add(Carousel(id="c2", name="Carousel Deluxe", min_height_cm=0, animals=["Tiger", "Bear", "Giraffe"]))

print(park.list_all())