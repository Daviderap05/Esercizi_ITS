import re

def mask_numbers(text: str):
    
    print(re.sub(r'\d', "#",  text))

text: str = "Il codice è 12345 e la data è 2025."
mask_numbers(text)