reddito: int = int (input("inserisci il reddito familiare: "))
media: int = int (input("inserisci la media: "))

if reddito < 20000 and media > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio rifiutata (motivo: reddito o media insufficiente)")
    