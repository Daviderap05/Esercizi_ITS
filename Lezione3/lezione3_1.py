#2.3


# name: str = "Davide"
# print(f"Hello {name}, would you like to learn some Python today?")


#2.4


# name: str = "Davide"

# print(name.upper())
# print(name.lower())
# print(name.title())


#2.5 / 2.6


# name: str = "Albert Einstein"
# quote: str = "A person who never made a mistake never tried anything new."

# print(f"{name} once said, {quote}")


#3.1 / 3.2


# names: list = ["Davide", "Matteo", "Gabriele", "Tommaso"]

# for name in names:
    
#     print("Hello " + name)


#3.3


# names: list = ["Ducati", "Honda", "Kawasaki"]

# for name in names:
    
#     print(f"I would like to own a {name} motorcycle.") 


#3.4 / 3.5 / 3.6 / 3.7 / 3.9


# names: list = ["Davide", "Matteo", "Gabriele"]

# for name in names:
    
#     print("Hello " + name + ", you've been invited to dinner")

# print("Gabriele won't be able to come to the dinner")

# names.remove("Gabriele")

# print("Hello Tommaso, you've been invited to dinner")
# print("Tommaso will be able to come to the dinner")

# names.append("Tommaso")

# print("Greate news... we can invite more people (I request a new answers)")

# names.insert(0, "Federico")
# names.insert((len(names) // 2), "Lorenzo")
# names.append("Francesco")

# for name in names:
    
#     print("Hello " + name + ", you've been invited to dinner")
    
# print("Now, in total, the number of guests is: " + str(len(names)))
    
# print("We're sorry, but unfortunately we can only invite two people")

# for name in reversed(names):
    
#     if len(names) > 2:
        
#         print(name + " unfortunately you will no longer be able to come to dinner")
#         names.pop()
    
# for name in names:
        
#     print(name + " you are still invited to the dinner")
    
# del names [0 : ]

# print(names)


#3.8


# places: list = ["Maldives", "Dubai", "Paris", "Germany", "America"]

# print(places)

# print(sorted(places))

# print(places)

# places.reverse()

# print(places)

# places.reverse()

# print(places)

# places.sort()

# print(places)

# places.sort()

# print(places)

# places.sort(reverse= True)

# print(places)


#6.1 / 6.7


# person1 = {
#     "first_name": "Mario",
#     "last_name": "Rossi",
#     "age": 18,
#     "city": "Roma"
# }

# person2 = {
#     "first_name": "Leonardo",
#     "last_name": "Borgioni",
#     "age": 20,
#     "city": "Fiumicino"
# }

# person3 = {
#     "first_name": "Matteo",
#     "last_name": "Agli",
#     "age": 19,
#     "city": "Focene"
# }

# print(f"First Name: {person1['first_name']}")
# print(f"Last Name: {person1['last_name']}")
# print(f"Age: {person1['age']}")
# print(f"City: {person1['city']}")

# people: list = [person1, person2, person3]

# for person in people:
    
#     for key, value in person.items():
        
#         print(f"{key}: {value}")

#     print()

        
#6.2 / 6.10


# favorite_numbers = {
#     "Davide": [7, 5, 9, 3],
#     "Matteo": [9, 1, 4, 0],
#     "Gabriele": [2, 6, 9, 3],
#     "Tommaso": [8, 5, 3, 6],
#     "Lorenzo": [7, 2, 1, 9]
# }


# for name, numbers in favorite_numbers.items():

#     print(f"{name}'s favorite number is:")
    
#     for number in numbers:
        
#         print(f"- {number}")


# 6.3


# glossary = {
#     "Variabile": "Un'area di memoria che contiene un valore che può cambiare durante l'esecuzione del programma.",
#     "Funzione": "Un blocco di codice che esegue un compito specifico e può essere richiamato da altre parti del programma.",
#     "Ciclo": "Una struttura di controllo che permette di eseguire ripetutamente un blocco di codice.",
#     "Lista": "Una collezione ordinata di elementi che può contenere valori di qualsiasi tipo.",
#     "Dizionario": "Una collezione di coppie chiave-valore, dove ogni chiave è unica e viene utilizzata per accedere al valore corrispondente."
# }

# for term, meaning in glossary.items():
#     print(f"{term}:\n{meaning}\n")


#6.8


# pet1 = {
#     "kind": "Cane",
#     "owner": "Davide"
# }

# pet2 = {
#     "kind": "Gatto",
#     "owner": "Matteo"
# }

# pet3 = {
#     "kind": "Coniglio",
#     "owner": "Gabriele"
# }

# pet4 = {
#     "kind": "Pappagallo",
#     "owner": "Tommaso"
# }

# pet5 = {
#     "kind": "Pesce",
#     "owner": "Lorenzo"
# }

# pets = [pet1, pet2, pet3, pet4, pet5]

# for pet in pets:
    
#     for key, value in pet.items():
        
#         print(f"{key}: {value}")
        
#     print()


#6.9


# favorite_places = {
#     "Davide": ["Maldives", "Paris", "New York"],
#     "Matteo": ["Tokyo", "Berlin"],
#     "Gabriele": ["Rome", "London", "Barcelona"]
# }

# for name, places in favorite_places.items():
    
#     print(f"{name}'s favorite places are:")
    
#     for place in places:
        
#         print(f"- {place}")
        
#     print()
    

#6.11


# cities = {
#     "Roma": {
#         "country": "Italia",
#         "population": "2.8 mln",
#         "fact": "Roma è conosciuta come la Città Eterna."
#     },
#     "Tokyo": {
#         "country": "Giappone",
#         "population": "37.4 mln",
#         "fact": "Tokyo è la città più popolosa del mondo."
#     },
#     "New York": {
#         "country": "Stati Uniti",
#         "population": "8.4 mln",
#         "fact": "New York è conosciuta come la Grande Mela."
#     }
# }

# for city, info in cities.items():
    
#     print(f"{city}:")
    
#     for key, value in info.items():
        
#         print(f"  {key}: {value}")
        
#     print()

#3.10 / 6.12 per noia non fatti
