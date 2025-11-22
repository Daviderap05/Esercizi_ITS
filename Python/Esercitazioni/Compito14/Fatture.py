from Paziente import Paziente
from Dottore import Dottore


class Fattura:
    def __init__(self, patients: list[Paziente], doctor: Dottore) -> None:
        if doctor.isAValidDoctor() and isinstance(patients, list) and isinstance(doctor, Dottore):
            self.doctor: Dottore | None = doctor
            self.patients: list[Paziente] | None = patients
            self.fatture: int | None = len(self.patients)
            self.salary: int | float | None = 0
        else:
            self.doctor = None
            self.patients = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self) -> int | float | None:
        if self.doctor is None or self.patients is None:
            self.salary = None
            return None

        parcella = self.doctor.getParcella()
        num = self.getFatture()
        if parcella is None or num is None:
            self.salary = None
            return None

        self.salary = parcella * num
        return self.salary

    def getFatture(self) -> int | None:
        if self.patients is None:
            self.fatture = None
            return None
        self.fatture = len(self.patients)
        return self.fatture

    def addPatient(self, newPatient: Paziente) -> None:
        if self.doctor is None or self.patients is None:
            print("Operazione non consentita: dottore non valido o fattura non inizializzata.")
            return

        if any(p.getIdCode() == newPatient.getIdCode() for p in self.patients): # any retituisce true se un controlla nel for da true
            self.patients.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(
                f"Alla lista del Dottor {self.doctor.getLastname()} "
                f"è stato aggiunto il paziente {newPatient.getIdCode()}"
            )
        else:
            print("Attenzione il paziente è gia presente nella lista.")

    def removePatient(self, idCode: str) -> None:
        if self.doctor is None or self.patients is None:
            print("Operazione non consentita: dottore non valido o fattura non inizializzata.")
            return

        for p in self.patients:
            if p.getIdCode() == idCode:
                self.patients.remove(p)
                self.getFatture()
                self.getSalary()
                print(
                    f"Alla lista del Dottor {self.doctor.getLastname()} "
                    f"è stato rimosso il paziente {idCode}"
                )
                break