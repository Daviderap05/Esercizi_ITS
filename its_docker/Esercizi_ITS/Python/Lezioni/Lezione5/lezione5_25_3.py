favorite_places: dict[str, list[str]] = {
    
    "Alessandro": ["Roma", "Parigi", "New York"],
    "Bianca": ["Londra", "Tokyo", "Cairo"],
    "Carlo": ["Barcellona", "Berlino", "Amsterdam"]
    
}

for person, places in favorite_places.items():
    
    print(f"I luoghi preferiti di {person} sono:")
    
    for place in places:
        
        print(f"- {place}")
        
    print("")