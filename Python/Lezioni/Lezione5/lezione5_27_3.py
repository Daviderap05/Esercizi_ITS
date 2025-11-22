cities: dict[str, dict[str, str | int]] = {
    "Roma": {
        "country": "Italia",
        "population": 2873000,
        "fact": "Roma è conosciuta come la Città Eterna."
    },
    
    "Parigi": {
        "country": "Francia",
        "population": 2148000,
        "fact": "Parigi è famosa per la Torre Eiffel."
    },
    
    "New York": {
        "country": "Stati Uniti",
        "population": 8419000,
        "fact": "New York è conosciuta come la Grande Mela."
    }
}

for city, info in cities.items():
    
    print(f"{city}:")
    
    for key, value in info.items():
        
        print(f"  {key.title()}: {value}")
        
    print("")