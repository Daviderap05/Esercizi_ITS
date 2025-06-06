class Date:
    
    def __init__(self, giorno: int = 0, mese: int = 0, anno: int = 0):
        
        self.giorno = giorno
        self.mese = mese
        self.anno = anno
        self.listaDate: list[str] = []
        
        
    def displayDate(self):
        
        if not self.listaDate:
            
            print("Nessuna data inserita.\n")
            return False
            
        else:
            
            for i in range(len(self.listaDate)):
                
                print(f"{i + 1}° data: {self.listaDate[i]}")
            
            print("")
            
            return True
        
                
    def createDate(self):
        
        while True:
            
            try:
                
                self.anno: int = int(input("Inserisci un anno valido (1908 --> 2025): "))
                
                if not(1908 <= self.anno <= 2025):
                    
                    raise ValueError("anno non valido... riprovare")
                
                self.mese: int = int(input("\nInserisci un mese valido (1 --> 12): "))
                
                if not(1 <= self.mese <= 12):
                    
                    raise ValueError("mese non valido... riprovare")
                
                if self.anno == 2025 and self.mese >= 5: 
                    
                    raise ValueError("mese non valido... riprovare")
                
                self.giorno: int = int(input("\nInserisci un giorno valido (1 --> 31): "))
                
                if not(1 <= self.giorno <= 31):
                    
                    raise ValueError("giorno non valido... riprovare")
                
                if (self.giorno > 28 and self.mese == 2) or (self.giorno > 30 and self.mese in [4, 6, 9, 11]):
                
                    raise ValueError("giorno non valido... riprovare")
                
                data: str = f"{self.giorno:02d} / {self.mese:02d} / {self.anno}"
                self.listaDate.append(data)
                
                print(f"\nOperazione effettuata con successo\n")
                
            except ValueError as e:
                
                print(e, end="\n\n")
                
            else:
                
                break
            
            
    def deleteDate(self):
        
        while True:
            
            if not self.displayDate():
                
                break
                    
            try:
                
                d: int = int(input("Inserisci il numero della data da eliminare: "))
                
                if 1 <= d <= len(self.listaDate):
                    
                    print(f"\nData rimossa: {self.listaDate[d-1]}\n")
                    self.listaDate.pop(d-1)
                    
                else:
                    
                    raise ValueError("Indice non valido... riprovare")
                                
            except ValueError as e:
            
                print(e, end="\n\n")
                
            else:
                
                break
           
            
    def editDate(self):
        
        while True:
            
            if not self.displayDate():
                
                break
                    
            try:
                
                m: int = int(input("Inserisci il numero della data da modificare: "))
                
                if 1 <= m <= len(self.listaDate):
                    
                    print("")
                    self.createDate()
                    
                else:
                    
                    raise ValueError("Indice non valido... riprovare")
                
                self.listaDate[m-1] = self.listaDate[-1]
                self.listaDate.pop()
                
                print(f"Data modificata: {self.listaDate[m-1]}\n")
                
            except ValueError as e:
            
                print(e, end="\n\n")
                
            else:
                
                break
     
    
    @classmethod
    def main(cls):
    
        opzione: int = 0
        o_data: Date = Date()
        
        while opzione != 5:
        
            print("1 --> Visualizza le date inserite")
            print("2 --> Inserisci una data")
            print("3 --> Modifica una data")
            print("4 --> Elimina una data")
            print("5 --> Esci dal programma\n")
            
            while True:
            
                try:
                    
                    opzione: int = int(input("Scegliere il numero dell'operazione da effettuare: "))
                        
                except ValueError:
                    
                    print("Opzione non valida... riprova.\n")
                    
                else:
                    
                    break        
            
            print("")

            match opzione:
                
                case 1:
                    
                    o_data.displayDate()
                        
                case 2:
                    
                    o_data.createDate()
                        
                case 3:
                    
                    o_data.editDate()
                    
                case 4:
                    
                    o_data.deleteDate()
                    
                case 5:
                    
                    print("Addio")
                    
                case _:
                    
                    print("Numero non valido... riprova\n")
                    
    
    
if __name__ == "__main__":
    
    Date.main()