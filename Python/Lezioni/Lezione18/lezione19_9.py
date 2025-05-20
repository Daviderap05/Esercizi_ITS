import string

def encryption(text: str):
    
    if text and text.isalpha():
        
        while True:
            
            try:
                
                num: int = int(input("Inserire la chiave: "))
                
            except ValueError:
                
                print("inseirire un numero... riprova\n")
                
            break
        
        alphabet_dict: dict[str, int] = {letter: index for index, letter in enumerate(string.ascii_lowercase, start=1)}
        text_c: str = ""
        
        # prima trasforma in list il text
        #poi uso 2 for
        #uno per i caratteri del text
        #l'altro per entrare nel dizionario e con qualche if criptare
        list(text)
        
        #print(text_c)
        
    else:
        
        print("Inserire un testo valido con solamente lettere")


def decryption():
    
    pass   

encryption("ciao")