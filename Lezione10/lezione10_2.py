#esercizio 3 e 5

class User:
    
    #login_attempts: int = 0
    
    def __init__(self, first_name: str, last_name: str, age: int, email: str, city: str, login_attempts: int = 0):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = login_attempts

    def describe_user(self):
        
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Età: {self.age}")
        print(f"Email: {self.email}")
        print(f"Città: {self.city}")
        
    def greet_user(self):
        
        print(f"Ciao {self.first_name} {self.last_name}, benvenuto/a!")
    
    def increment_login_attempts(self):
        
        self.login_attempts += 1

        return self.login_attempts
    
    def reset_login_attempts(self):
        
        self.login_attempts = 0
        
        return self.login_attempts
    
    # @classmethod
    # def increment_login_attempts(cls):
        
    #     cls.login_attempts += 1

    #     return cls.login_attempts
    
    # @classmethod
    # def reset_login_attempts(cls):
        
    #     cls.login_attempts = 0
        
    #     return cls.login_attempts
        
user1 = User("Alice", "Rossi", 25, "alice.rossi@example.com", "Milano")
#print(User.increment_login_attempts())
print(user1.increment_login_attempts())

print("")

user2 = User("Bob", "Bianchi", 30, "bob.bianchi@example.com", "Roma")
#print(User.increment_login_attempts())
print(user2.increment_login_attempts())
print(user2.increment_login_attempts())
print(user2.increment_login_attempts())
print(user2.increment_login_attempts())

print("")

user1.describe_user()
user1.greet_user()

print("")

user2.describe_user()
user2.greet_user()

print("")

#print(User.reset_login_attempts())
print(user1.reset_login_attempts())
print(user2.reset_login_attempts())