import re

def extract_emails(text: str):
    
    print(re.findall(r'\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.]+\.[a-zA-Z]{2,}\b', text))
    
text: str = "Contattaci a info.ale@azienda.com oppure support@helporg"
extract_emails(text)