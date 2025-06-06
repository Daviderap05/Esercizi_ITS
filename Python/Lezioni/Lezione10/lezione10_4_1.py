class User:
    
    def __init__(self, first_name: str, last_name: str, username: str, email: str):
        
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        
        print(f"Ciao {self.first_name} {self.last_name}, benvenuto/a!")


class Privileges:
    
    def __init__(self, privileges: list[str]):
        
        self.privileges = privileges

    def show_privileges(self):
        
        print("Privilegi:")
        
        for privilege in self.privileges:
            
            print(f"- {privilege}")


class Admin:
    
    def __init__(self, user: User, privileges: Privileges):
        
        self.user = user
        self.privileges = privileges

    def describe_user(self):
        
        self.user.describe_user()

    def show_privileges(self):
        
        self.privileges.show_privileges()