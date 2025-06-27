#esercizio che parte da "lezione5_20_3"

from typing import Any  # import Any visto che i valori sono di diversi tipi

person1: dict[str, Any] = {
    "first_name": "Davide",
    "last_name": "Raponi",
    "age": 19,
    "city": "Rome"
}

for key, value in person1.items():
    
    print(f"{key} = {value}")
    
print("")

person2: dict[str, Any] = {
    "first_name": "Maria",
    "last_name": "Bianchi",
    "age": 25,
    "city": "Milan"
}

person3: dict[str, Any] = {
    "first_name": "Luca",
    "last_name": "Verdi",
    "age": 30,
    "city": "Naples"
}

people: list[dict[str, str]] = [person1, person2, person3]

for person in people:
    
    for key, value in person.items():
        
        print(f"{key} = {value}")
        
    print("")