import requests

BASE_URL = "http://localhost:5000"
headers = {"Content-type": "application/json", "Accept": "application/json"}
b_id = "BK-TEST-001"  # Variabile per l'ID, così lo scrivi una volta sola

if __name__ == "__main__":

    # 1) GET / (Home)
    print("\n1. GET /")
    r = requests.get(f"{BASE_URL}/", headers=headers)
    print(r.status_code, r.json())

    # 2) GET /bookings (Lista)
    print("\n2. GET /bookings")
    r = requests.get(f"{BASE_URL}/bookings", headers=headers)
    print(r.status_code, r.json())

    # 3) POST /bookings (Creazione)
    new_booking = {
        "booking_id": b_id,
        "type": "visit",
        "patient_name": "Mario Rossi",
        "doctor": "Dr. House",
        "department": "Cardio",
        "date": "2026-05-20",
        "time": "09:00",
        "status": "scheduled",
        "visit_reason": "Controllo",
        "first_time": True,
    }
    print("\n3. POST /bookings")
    r = requests.post(f"{BASE_URL}/bookings", headers=headers, json=new_booking)
    print(r.status_code, r.json())

    # 4) GET /bookings/<id> (Verifica esistenza)
    print(f"\n4. GET /bookings/{b_id}")
    r = requests.get(f"{BASE_URL}/bookings/{b_id}", headers=headers)
    print(r.status_code, r.json())

    # 5) PATCH /bookings/<id>/status (Modifica stato)
    patch_data = {"status": "checked_in"}
    print(f"\n5. PATCH /bookings/{b_id}/status")
    r = requests.patch(
        f"{BASE_URL}/bookings/{b_id}/status", headers=headers, json=patch_data
    )
    print(r.status_code, r.json())

    # 6) PUT /bookings/<id> (Sostituzione dati)
    # Copio i dati vecchi e cambio l'orario
    put_data = new_booking.copy()
    put_data["time"] = "18:00"

    print(f"\n6. PUT /bookings/{b_id}")
    r = requests.put(f"{BASE_URL}/bookings/{b_id}", headers=headers, json=put_data)
    print(r.status_code, r.json())

    # 7) DELETE /bookings/<id> (Cancellazione)
    print(f"\n7. DELETE /bookings/{b_id}")
    r = requests.delete(f"{BASE_URL}/bookings/{b_id}", headers=headers)
    print(r.status_code, r.json())

    # 8) GET /bookings/<id> (Verifica 404)
    print(f"\n8. GET post-delete /bookings/{b_id}")
    r = requests.get(f"{BASE_URL}/bookings/{b_id}", headers=headers)
    print(r.status_code, r.json())
