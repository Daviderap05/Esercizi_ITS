from Class.clinic_hub import ClinicHub
from Class.medical_visit import MedicalVisit
from Class.diagnostic_exam import DiagnosticExam


# 1. Creazione del sistema di gestione
hub = ClinicHub()
print("--- Sistema ClinicHub Inizializzato ---\n")

# 2. Creazione di una Visita Medica (MedicalVisit)
# Esempio: Paziente con dolore acuto (dovrebbe avere priorità alta)
visit1 = MedicalVisit(
    booking_id="BK-VISIT-001",
    patient_name="Mario Rossi",
    doctor="Dr. Bianchi",
    department="Cardiologia",
    date="2026-02-10",
    time="10:00",
    visit_reason="Dolore toracico acuto",
    first_time=True,
)

# 3. Creazione di un Esame Diagnostico (DiagnosticExam)
# Esempio: RMN (dovrebbe avere priorità alta)
exam1 = DiagnosticExam(
    booking_id="BK-EXAM-999",
    patient_name="Luigi Verdi",
    doctor="Dr. Neri",
    department="Radiologia",
    date="2026-02-11",
    time="14:30",
    exam_type="RMN",
    requires_fasting=False,
)

# 4. Aggiunta al Hub
print(f"Aggiunta visita {visit1.booking_id}: {hub.add(visit1)}")
print(f"Aggiunta esame {exam1.booking_id}: {hub.add(exam1)}")

# Tentativo di duplicato
print(f"Tentativo aggiunta duplicato {visit1.booking_id}: {hub.add(visit1)}")

print("\n--- Lista di tutte le prenotazioni ---")
for b in hub.list_all():
    print(b)

# 5. Test metodi specifici (Attesa stimata e Patch)
print("\n--- Dettagli Calcolo Attesa ---")

# Calcolo attesa per la visita (Dolore acuto -> priorità 7)
# Formula: 30 * 1.0 + 7 * 5 = 30 + 35 = 65 minuti
wait_v1 = visit1.estimated_wait()
print(f"Attesa stimata per {visit1.patient_name} (Visita): {wait_v1} min")

# Calcolo attesa per l'esame (RMN -> priorità 8)
# Formula: 45 * 1.5 (fattore es.) + 8 * 5 = 67.5 + 40 = 107 minuti (int)
wait_e1 = exam1.estimated_wait(factor=1.5)
print(f"Attesa stimata per {exam1.patient_name} (Esame, factor 1.5): {wait_e1} min")

# 6. Test Modifica Stato
print("\n--- Aggiornamento Stato ---")
hub.patch_status("BK-VISIT-001", "checked_in")
updated_visit = hub.get("BK-VISIT-001")
print(f"Nuovo stato per Mario Rossi: {updated_visit.status}")

# 7. Cancellazione
print("\n--- Cancellazione ---")
deleted = hub.delete("BK-EXAM-999")
print(f"Esame cancellato: {deleted}")
print(f"Prenotazioni rimanenti: {len(hub.list_all())}")