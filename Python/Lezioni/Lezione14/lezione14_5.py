import re

def find_dates(text: str):
    
    print(re.findall(r'\b(?:0[1-9]|[12][0-9]|3[01])/(?:0[1-9]|1[0-2])/[0-9]{4}\b', text))
    
text: str = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)