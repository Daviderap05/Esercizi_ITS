import re

def is_valid_cap(cap: str):
    
    result = re.fullmatch(r'^\d{5}$', cap)
    
    if result != None:
        
        print(True)
        
    else:
        
        print(False)

is_valid_cap("70124")
is_valid_cap("A0123")