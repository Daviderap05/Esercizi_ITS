import re

def check_product_code(code: str):
    
    result = re.fullmatch(r'^PROD-\d{4}-[A-Z]{2}$', code)
    
    if result != None:
        
        print(True)
        
    else:
        
        print(False)

check_product_code("PROD-9876-ZX") 
check_product_code("PROD-99-ZX")   