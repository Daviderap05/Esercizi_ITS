class InvalidPasswordError(Exception):

    @staticmethod
    def check_length(password: str):

        if len(password) < 20:
            
            raise InvalidPasswordError(f"La lunghezza della password deve essere di almeno 20 caratteri, invece è {len(password)}.")

    @staticmethod
    def check_uppercase(password: str):
        
        uppercase_count = sum(1 for char in password if char.isupper())
        
        if uppercase_count < 3:
            
            raise InvalidPasswordError(f"La password deve contenere almeno 3 lettere maiuscole, invece ne ha {uppercase_count}.")

    @staticmethod
    def check_special_characters(password: str):
        
        special_char_count = sum(1 for char in password if not char.isalnum())
        
        if special_char_count < 4:
            
            raise InvalidPasswordError(f"La password deve contenere almeno 4 caratteri speciali, invece ne ha {special_char_count}.")

def validate_password(password: str):
    
    InvalidPasswordError.check_length(password)
    InvalidPasswordError.check_uppercase(password)
    InvalidPasswordError.check_special_characters(password)
    
    print("Password valida!")

try:
    
    validate_password("PPPPiiiiiiiiiiiiiii12@@@")
    
except InvalidPasswordError as e:
    
    print(e)