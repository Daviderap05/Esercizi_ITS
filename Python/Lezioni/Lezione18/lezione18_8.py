class ATM():
    
    def __init__(self, balance: float = 0.0) -> None:
        
        self.balance = balance
        
        
    def deposit(self, num: float = 0.0):
        
        if isinstance(num, (int)) or isinstance(num, (float)) and num > 0:
            
            self.balance += num
            
            print(f"Hai depositato {num}$")
            self.check()
            
        else:
            
            print("Errore: Il valore deve essere un numero positivo.")
            
            
    def withdraw(self, num: float = 0.0):
        
        if isinstance(num, (int)) or isinstance(num, (float)) and num > 0:
            
            if (self.balance - num) >= 0.0:
                
                self.balance -= num
                
                print(f"Hai ritirato {num}$")
                self.check()
                
            else:
                
                print("Errore: Saldo insufficiente per completare il prelievo.")

        else:
            
            print("Valore non compatibile")
            
        
    def check(self):
        
        print(f"L'ammontare del conto è: {self.balance}$")