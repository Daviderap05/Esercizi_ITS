#5.1 / 5.2

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Altri test condizionali
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

print("\nIs car == 'toyota'? I predict False.")
print(car == 'toyota')

print("\nIs car != 'toyota'? I predict True.")
print(car != 'toyota')

print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)

print("\nIs len(car) == 5? I predict False.")
print(len(car) == 5)

print("\nIs car.startswith('s')? I predict True.")
print(car.startswith('s'))

print("\nIs car.endswith('u')? I predict False.")
print(car.endswith('u'))

# Test di uguaglianza e disuguaglianza con stringhe
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

# Test usando il metodo lower()
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car.lower() == 'SUBARU'? I predict False.")
print(car.lower() == 'SUBARU')

# Test numerici di uguaglianza e disuguaglianza, maggiore di e minore di, maggiore o uguale a e minore o uguale a
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age != 25? I predict False.")
print(age != 25)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 20? I predict False.")
print(age < 20)

print("\nIs age >= 25? I predict True.")
print(age >= 25)

print("\nIs age <= 20? I predict False.")
print(age <= 20)

# Test usando le parole chiave and e or
print("\nIs age > 20 and age < 30? I predict True.")
print(age > 20 and age < 30)

print("\nIs age < 20 or age > 30? I predict False.")
print(age < 20 or age > 30)

# Test se un elemento è in una lista
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'apple' in fruits? I predict True.")
print('apple' in fruits)

print("\nIs 'orange' in fruits? I predict False.")
print('orange' in fruits)

# Test se un elemento non è in una lista
print("\nIs 'orange' not in fruits? I predict True.")
print('orange' not in fruits)

print("\nIs 'banana' not in fruits? I predict False.")
print('banana' not in fruits)