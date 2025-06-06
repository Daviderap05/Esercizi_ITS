from lezione10_4_1 import *

user: User = User("Alice", "Rossi", "ciccio", "alice.rossi@example.com")

privileges: Privileges = Privileges(["View audit log", "See history", "Manage channels"])

admin: Admin = Admin(user, privileges)

admin.describe_user()
admin.show_privileges()