i: int = 0

while True:
    
    parola: str = input(f"inserire la {i + 1}° parola: ")
    
    if parola == "fine":
        
        break
    
    elif parola[0] == parola [-1]:
        
        print(f"La parola '{parola}' ha la prima e ultima lettera uguali\n")
    
    else:
        
        print(f"La parola '{parola}' non ha la prima e ultima lettera uguali\n")
        
    i += 1