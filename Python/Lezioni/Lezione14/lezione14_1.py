import re

def is_integer(s: str):
    
    result = re.fullmatch(r'-?\d+', s)
    
    if result != None:
        
        print(True)
        
    else:
        
        print(False)
    
is_integer("123")    
is_integer("-456")     
is_integer("12.3")