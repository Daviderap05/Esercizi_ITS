# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo.
 
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti.
 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 
# 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 10 euro, 5 euro e/o 
# in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro 
# sono necessarie per pagare l'importo in contanti.

from Pagamento import Pagamento


class PagamentoContanti(Pagamento):
    
    def __init__(self, importo: float) -> None:
        super().__init__()
        
        self.setImporto(importo)
        
        
    def dettagliPagamento(self) -> None:
        print(f"pagamento in contanti di: €{self.getImporto():.2f}")
     
        
    def inPezziDa(self) -> None:
        
        importo: float = self.getImporto()
        cont: int = 0
        
        diz_banconote_monete: dict[int, int|float] = {
            1: 500,
            2: 200,
            3: 100,
            4: 50,
            5: 20,
            6: 10,
            7: 5,
            8: 2,
            9: 1,
            10: 0.50,
            11: 0.20,
            12: 0.10,
            13: 0.05,
            14: 0.01
        }
        
        print(f"{self.getImporto()} euro da pagare in contanti con:")
        for key, value in diz_banconote_monete.items():
                
            while True:
                
                if round(importo, 2) - value >= 0:
                    
                    importo -= value
                    cont += 1
                
                else: 
                    
                    if cont != 0:
                        
                        if key < 8:
                            
                            if cont == 1:
                                print(f"{cont} banconota da: {value} euro")
                            else:
                                print(f"{cont} banconote da: {value} euro")
                        else:
                            
                            if cont == 1:
                                print(f"{cont} moneta da: {value} euro")
                            else:
                                print(f"{cont} monete da: {value} euro")
                        
                    cont = 0
                    break