# driver.py
from Dottore import Dottore
from Paziente import Paziente
from Fatture import Fattura

if __name__ == "__main__":
    # --- Dottori ---
    dottore_1 = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
    dottore_1.setAge(45)  # deve risultare valido

    dottore_2 = Dottore("Giulia", "Bianchi", "Dermatologa", 120.0)
    dottore_2.setAge(36)  # deve risultare valido

    # Presentazione dei medici
    dottore_1.doctorGreet()
    dottore_2.doctorGreet()

    # --- Pazienti ---
    # Lista 1: 3 pazienti
    p1 = Paziente("Anna", "Verdi", "A1")
    p2 = Paziente("Luca", "Neri", "B2")
    p3 = Paziente("Sara", "Galli", "C3")
    lista_pazienti_1 = [p1, p2, p3]

    # Lista 2: 1 paziente
    p4 = Paziente("Paolo", "Blu", "D4")
    lista_pazienti_2 = [p4]

    # --- Fatture ---
    fattura1 = Fattura(lista_pazienti_1, dottore_1)
    fattura2 = Fattura(lista_pazienti_2, dottore_2)

    # Stampa salari iniziali
    salario1 = fattura1.getSalary()
    salario2 = fattura2.getSalary()
    print(f"Salario Dottore1: {salario1} euro!")
    print(f"Salario Dottore2: {salario2} euro!")

    # Sposta un paziente (es. B2) da dottore_1 a dottore_2
    fattura1.removePatient("B2")  # rimuove dal primo
    fattura2.addPatient(p2)       # aggiunge al secondo

    # Stampa salari dopo lo spostamento
    salario1 = fattura1.getSalary()
    salario2 = fattura2.getSalary()
    print(f"Salario Dottore1: {salario1} euro!")
    print(f"Salario Dottore2: {salario2} euro!")

    # Guadagno totale dell'ospedale
    totale = (salario1 or 0) + (salario2 or 0)
    print(f"In totale, l'ospedale ha incassato: {totale} euro!")
