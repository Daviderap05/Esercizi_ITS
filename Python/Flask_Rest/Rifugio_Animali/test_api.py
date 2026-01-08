import requests
import json

BASE_URL = "http://127.0.0.1:5000"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def print_response(title: str, response: requests.Response) -> None:
    """Stampa titolo, status code e JSON (se possibile)."""
    print(f"\n=== {title} ===")
    print(f"Status: {response.status_code}")
    try:
        data = response.json()
        print("Body:")
        print(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        # La risposta non è JSON
        print("Body (non JSON):")
        print(response.text)


def main():
    # 1) GET /
    resp = requests.get(f"{BASE_URL}/")
    print_response("GET /", resp)

    # 2) GET /animals
    resp = requests.get(f"{BASE_URL}/animals")
    print_response("GET /animals", resp)

    dog_id: str = "d1"

    # 3) GET /animals/d1
    resp = requests.get(f"{BASE_URL}/animals/{dog_id}")
    print_response(f"GET /animals/{dog_id}", resp)

    # 4) GET /animals/d1/food
    resp = requests.get(f"{BASE_URL}/animals/{dog_id}/food")
    print_response(f"GET /animals/{dog_id}/food", resp)

    # 5) GET /animals/d1/adoption
    resp = requests.get(f"{BASE_URL}/animals/{dog_id}/adoption")
    print_response(f"GET /animals/{dog_id}/adoption", resp)

    # 6) POST /animals/add – aggiunta di un nuovo cane
    new_dog = {
        "type": "dog",
        "id": "d3",
        "name": "Rex",
        "age_years": 2,
        "weight_kg": 18.5,
        "breed": "border collie",
        "is_trained": True,
    }

    resp = requests.post(
        f"{BASE_URL}/animals/add",
        headers=headers,
        json=new_dog,
    )
    print_response("POST /animals/add (new dog)", resp)

    # Verifica con GET /animals/d3
    resp = requests.get(f"{BASE_URL}/animals/{new_dog['id']}")
    print_response(f"GET /animals/{new_dog['id']}", resp)

    # 7) POST /animals/add – aggiunta di un nuovo gatto
    new_cat = {
        "type": "cat",
        "id": "c2",
        "name": "Micia",
        "age_years": 3,
        "weight_kg": 4.2,
        "indoor_only": True,
        "favorite_toy": "ball",
    }

    resp = requests.post(
        f"{BASE_URL}/animals/add",
        headers=headers,
        json=new_cat,
    )
    print_response("POST /animals/add (new cat)", resp)

    # Verifica con GET /animals/c2
    resp = requests.get(f"{BASE_URL}/animals/{new_cat['id']}")
    print_response(f"GET /animals/{new_cat['id']}", resp)

    # 8) POST /animals/<animal_id>/adopt – registrare l’adozione del nuovo cane
    adoption_payload = {
        "adopter_name": "Mario Rossi",
    }

    resp = requests.post(
        f"{BASE_URL}/animals/{new_dog['id']}/adopt",
        headers=headers,
        json=adoption_payload,
    )
    print_response(f"POST /animals/{new_dog['id']}/adopt", resp)

    # Subito dopo, GET /animals/d3/adoption per verificare adopted: true
    resp = requests.get(f"{BASE_URL}/animals/{new_dog['id']}/adoption")
    print_response(f"GET /animals/{new_dog['id']}/adoption", resp)


if __name__ == "__main__":
    main()
