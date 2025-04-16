import re

def find_codes(text: str):
    
    print(re.findall(r'[a-zA-Z0-9]{8}', text))

text: str = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ supercal"
find_codes(text)