import string


def encryption(text: str, key: int = 3) -> str:
    
    if text:
        
        alphabet: str = string.ascii_lowercase
        text_c: str = ""
        
        for letter in text.lower():
            
            if letter in alphabet:
                
                index_c: int = (alphabet.index(letter) + key) % 26   #Da ricordare che quetsa operazione modulo permette di ricominciare la lista
                text_c += alphabet[index_c]
                
            else:
                
                text_c += letter
        
        return f"Testo cifrato: {text_c}"
        
    else:
        
        return "Inserire un testo valido con solamente lettere"


def decryption(text: str, key: int = 3) -> str:
    
    alphabet: str = string.ascii_lowercase   
    text_dc: str = ""
    
    for letter in text.lower():
            
            if letter in alphabet:
                
                index_c: int = (alphabet.index(letter) - key) % 26
                text_dc += alphabet[index_c]
                
            else:
                
                text_dc += letter
        
    return f"Testo decifrato: {text_dc}"


print(encryption("Ciao ho 9 anni@"))
print(decryption("fldr kr 9 dqql@"))