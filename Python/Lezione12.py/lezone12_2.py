def validate_password(password: str):
    
    cont: int = 0
    
    if len(password) > 20 and cont >= 3:
        pass
        
    for p in password: 
        
        if p.isupper():
            
            cont += 1
