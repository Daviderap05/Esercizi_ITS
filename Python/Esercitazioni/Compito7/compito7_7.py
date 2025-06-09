class ContactManager:
    
    def __init__(self, contacts: dict[str, list[str]] = {}) -> None:
        
        self.contacts: dict[str, list[str]] = contacts
        
        
    def __str__(self) -> str:
        
        return str(self.contacts)
        
        
    def create_contact(self, name: str, phone_numbers: list[str]) -> dict|str:
        
        if name in self.contacts:
            
            raise ValueError("Errore: il contatto esiste già.")
        
        self.contacts[name] = phone_numbers
        
        return {name : phone_numbers}
    
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict|str:
        
        if contact_name not in self.contacts:
            
            raise ValueError("Errore: il contatto non esiste.")
        
        if phone_number in self.contacts[contact_name]:
            
            raise ValueError("Errore: il numero di telefono esiste già.")
            
        self.contacts[contact_name].append(phone_number)
        
        return {contact_name : self.contacts[contact_name]}
    
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict|str:

        if contact_name not in self.contacts:
            
            raise ValueError("Errore: il contatto non esiste.")
        
        if phone_number not in self.contacts[contact_name]:
            
            raise ValueError("Errore: il numero di telefono non è presente.")
        
        self.contacts[contact_name].remove(phone_number)
        
        return {contact_name : self.contacts[contact_name]}
    
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict|str:
        
        if contact_name not in self.contacts:
            
            raise ValueError("Errore: il contatto non esiste.")
        
        if old_phone_number not in self.contacts[contact_name]:
            
            raise ValueError("Errore: il numero di telefono non è presente.")
        
        index_old_phone_number = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index_old_phone_number] = new_phone_number
        
        return {contact_name : self.contacts[contact_name]}


    def list_contacts(self) -> list[str]:
        
        return list(self.contacts.keys())        
        
        
    def list_phone_numbers(self, contact_name: str) -> list[str]|str:
        
        if contact_name not in self.contacts:
            
            raise ValueError("Errore: il contatto non esiste.")
        
        return self.contacts[contact_name]
        
        
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]|str:
        
        lista_occorrenze: list[str] = []
        
        for key in self.contacts.keys():
            
            if phone_number in self.contacts[key]:
                
                lista_occorrenze.append(key)
                
        
        if lista_occorrenze == []:
            
            raise ValueError("Nessun contatto trovato con questo numero di telefono.")
                
        return lista_occorrenze
        
        
        
registro: ContactManager = ContactManager()

print(registro.create_contact("Davide", ["2222222222", "22222222223"]))
print(registro.create_contact("mario", ["2222222222", "2222222222"]))
# print(registro.add_phone_number("Davide", "222222222"))
# print(registro.remove_phone_number("Davide", "222222222"))
print(registro.update_phone_number("Davide", "2222222222", "3333333333"))
print(registro.list_contacts())
print(registro.list_phone_numbers("Davide"))
print(registro.search_contact_by_phone_number("22222222223"))

print(registro)