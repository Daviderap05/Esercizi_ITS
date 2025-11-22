import string


def encryption(text: str, key: int = 3) -> str:
    
    if text:
        
        #text = text.replace(" ", "").lower()   comodo per sostituire a volte per eliminare gli spazi
        alphabet: str = string.ascii_lowercase
        text_c: str = ""
        
        for letter in text:
            
            if letter in alphabet:
                
                index_c: int = (alphabet.index(letter) + key) % 26   #modulo permette di ricominciare la lista
                text_c += alphabet[index_c]
        
        return f"Testo cifrato: {text_c}"
        
    else:
        
        return "Inserire un testo valido con solamente lettere"


def decryption(text: str, key: int = 3) -> str:
    
    alphabet: str = string.ascii_lowercase   
    text_dc: str = ""
    
    for letter in text:
            
            if letter in alphabet:
                
                index_dc: int = (alphabet.index(letter) - key) % 26
                text_dc += alphabet[index_dc]
                
            else:
                
                text_dc += letter
        
    return f"Testo decifrato: {text_dc}"

print(encryption("ciao ho 9 anni"))
print(decryption("fldrkrdqql"))