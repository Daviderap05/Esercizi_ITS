import re

def is_valid_ipv4(address: str) -> bool:
    
    ipv4_regex: str = r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    
    return bool(re.fullmatch(ipv4_regex, address))


#esercizi professore
def is_valid_ipv42(address: str) -> bool:
    
    address_s = address.split(".")
    
    if len(address_s) != 4:
        
        # raise ValueError("Errore, l'indirizzo è mal formato")
        return False
    
    for blocco in address_s:
        
        # raise ValueError("Errore, l'indirizzo contiene un carattere alfabetico!")
        if not blocco.isdigit():
            
            return False
        
        # raise ValueError("Errore, l'indirizzo non è compreso tra 0 e 255!")
        if not (0 <= int(blocco) <= 255):
            
            return False
        
    return True



print(is_valid_ipv4("192.168.0.1"))  # True
print(is_valid_ipv4("1.1.0.1"))  # True
print(is_valid_ipv4("255.255.255.255"))  # True
print(is_valid_ipv4("256.100.10.1"))  # False (256 è fuori range)
print(is_valid_ipv4("192.168.1"))  # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a"))  # False (parte non numerica)