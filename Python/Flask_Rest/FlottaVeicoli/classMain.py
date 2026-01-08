from Class.fleetManager import FleetManager
from Class.car import Car
from Class.van import Van


def main():
    # 1) Creo il gestore flotta
    fleet = FleetManager()

    # 2) Creo almeno due veicoli: una Car e un Van
    car1 = Car(
        plate_id="AB 123 CD",
        model="Fiat Panda",
        registration_year=2020,
        status="available",
        driver_name="Marco",
        doors=5,
        is_cabrio=False,
    )

    van1 = Van(
        plate_id="EF 456 GH",
        model="Iveco Daily",
        registration_year=2019,
        max_load_kg=4200,  # > 3500 -> richiede patente C
        status="maintenance",
        driver_name="Luca",
    )

    # 3) Li aggiungo alla flotta
    fleet.add(car1)
    fleet.add(van1)

    # 4) Stampo la lista completa
    print("\n--- VEICOLI IN FLOTTA ---")
    for v in fleet.list_all():
        print(v)

    # 5) (opzionale) esempio patch status + tempo stimato prep
    fleet.patch_status("AB 123 CD", "cleaning")
    print("\n--- INFO CAR DOPO PATCH ---")
    print(fleet.get("AB 123 CD").info())
    print(fleet.get("AB 123 CD").estimated_prep_time())


if __name__ == "__main__":
    main()