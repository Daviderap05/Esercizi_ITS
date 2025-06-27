import re

def is_valid_name(name: str):
    
    result = re.match(r'[A-Z][a-z]{2}', name)
    
    if result != None:
        
        print(True)
        
    else:
        
        print(False)

is_valid_name("Marco")    
is_valid_name("marco")    
is_valid_name("Ma")