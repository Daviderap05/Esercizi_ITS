studenti: list[dict] = [
    {"nome": "Anna", "media": 28},
    {"nome": "Luca", "media": 25},
    {"nome": "Marco", "media": 30}
]

# o_d: list[dict] = sorted(studenti, key = lambda studenti: studenti.get("media"), reverse = True)
o_d: list[dict] = sorted(studenti, key=lambda studente: studente["media"], reverse=True)

print(o_d)