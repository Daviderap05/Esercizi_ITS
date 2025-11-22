# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 

# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, 
# e il numero della carta di credito. 
# 
# Infine, si ridefinisca il metodo dettagliPagamento() 
# per includere tutte le informazioni della carta di credito oltre all'importo del pagamento.

from Pagamento import Pagamento
import re


class PagamentoCartaDiCredito(Pagamento):
    
    def __init__(self, importo: float, nome: str, data_scadenza: str, numero_carta: str) -> None:
        super().__init__()
        
        self.setImporto(importo)
        
        if nome and isinstance(nome, str):
            self.nome: str = nome
        else:
            raise ValueError ("Errore, nome non valido")
        
        if data_scadenza and isinstance(data_scadenza, str) and re.match(r"^(0[1-9]|1[0-2])\/\d{2}$", data_scadenza):
            self.data_scadenza: str = data_scadenza
        else:
            raise ValueError ("Errore, data di scadenza non valida")
        
        if numero_carta and isinstance(numero_carta, str) and re.match(r"^\d{16}$", numero_carta):
            self.numero_carta: str = numero_carta        
        else:
            raise ValueError ("Errore, numero di carta non valida")
        
        
    def dettagliPagamento(self) -> None:
        print(f"Pagamento di: €{self.getImporto():.2f} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome}")
        print(f"Data di scadenza: {self.data_scadenza}")
        print(f"Numero della carta: {self.numero_carta}")