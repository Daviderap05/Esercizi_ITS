def validate_password(password: str):
    
    cont1: int = 0
    cont2: int = 0
    
    for p in password: 
        
        if p.isupper():
            
            cont1 += 1
            
        elif (p.isalnum()) == False:
            
            cont2 += 1
            
    if cont1 < 3:
        
        raise ValueError(f"Le lettere maiuscole dovrebbero essere 3 o più, invece sono {cont1}")
    
    elif cont2 < 4:
        
        raise ValueError(f"Le lettere non alfanumeriche dovrebbero essere 4 o più, invece sono {cont2}")
    
    elif len(password) < 20:
        
        raise ValueError(f"La lunghezza della password deve essere di 20 o più caratteri, invece sono {len(password)}")
    
    else:
        
        print("ciao")

try:
    
    validate_password("PPPPiiiiiiiiiiiiiii12@@@")
    
except ValueError as e:

    print(e)