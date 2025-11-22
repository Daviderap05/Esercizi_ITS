current_users: list[str] = ["Mario", "Piero", "Davide", "Matteo", "Chiara"]
new_users: list[str] = ["Mario", "piero", "Alessandro", "Mattia", "Daniele"]
current_users_lowercase: list[str] = []

for user in current_users:
    
    current_users_lowercase.append(user.lower())

for i in new_users:
    

    if i.lower() in current_users_lowercase:
            
        print("Inserire nuovo nome utente")
        
    else:
            
        print("Nome utente disponibile")