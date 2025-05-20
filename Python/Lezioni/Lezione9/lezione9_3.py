class Person:
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

if alice.age > bob.age:
    
    print("Il nome della persona più grande è: " + alice.name)
    
else:
    
    print("Il nome della persona più grande è: " + bob.name)

charlie = Person("Charlie D.", 29)
diana = Person("Diana P.", 52)
edward = Person("Edward L.", 41)

persons: list[Person] = ([alice, bob, charlie, diana, edward])

#persons.extend comodo quando si voglino aggiungere più cose nella lista

age_p: str = ""
age_min: int = persons[0].age

for person in persons:
    
    if age_min > person.age:
        
        age_min = person.age
        age_p = person.name
    
print("Il/la più piccolo/a è: " + age_p)    