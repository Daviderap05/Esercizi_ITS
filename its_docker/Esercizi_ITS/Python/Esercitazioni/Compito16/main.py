# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito 
# con valori differenti e si invochi dettagliPagamento() per ognuno di essi.

# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro
# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro
# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456
# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321


from PagamentoContanti import PagamentoContanti
from PagamentoCartaDiCredito import PagamentoCartaDiCredito

if __name__ == "__main__":
    
    # Pagamenti in contanti
    p1 = PagamentoContanti(150.00)
    p2 = PagamentoContanti(95.25)

    p1.dettagliPagamento()
    p1.inPezziDa()
    print()

    p2.dettagliPagamento()
    p2.inPezziDa()
    print()

    # Pagamenti con carta di credito
    c1 = PagamentoCartaDiCredito(200.00, "Mario Rossi", "12/24", "1234567890123456")
    c2 = PagamentoCartaDiCredito(500.00, "Luigi Bianchi", "01/25", "6543210987654321")

    c1.dettagliPagamento()
    print()
    
    c2.dettagliPagamento()
    print()