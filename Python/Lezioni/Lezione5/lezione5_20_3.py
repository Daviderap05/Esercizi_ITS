from typing import Any     #import Any visto che i valori nsono di diversi tipi

people: dict[str : Any] = {
    
    "first_name" : "Davide", 
    "last_name" : "Raponi", 
    "age" : 19,
    "city" : "Rome"
    
}

for key, value in people.items():
    
    print(f"{key}  =  {value}")