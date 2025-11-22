people: dict[str : list[int]] = {
    
    "Matteo" : [5, 8, 2, 5], 
    "Gabriele" : [15, 34, 12, 11], 
    "Tommaso" : [45, 67, 23, 45],
    "Davide" : [51, 89, 62, 69]
    
}

for key, value in people.items():
    
    print("I numeri preferiti di " + key + " sono: " + ", ".join(map(str, value)))