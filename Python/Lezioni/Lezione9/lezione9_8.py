class User:
    
    def __init__(self, first_name: str, last_name: str, age: int, email: str, city: str):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Età: {self.age}")
        print(f"Email: {self.email}")
        print(f"Città: {self.city}")
        
    def greet_user(self):
        
        print(f"Ciao {self.first_name} {self.last_name}, benvenuto/a!")
        
user1 = User("Alice", "Rossi", 25, "alice.rossi@example.com", "Milano")
user2 = User("Bob", "Bianchi", 30, "bob.bianchi@example.com", "Roma")

user1.describe_user()
user1.greet_user()

print("")

user2.describe_user()
user2.greet_user()