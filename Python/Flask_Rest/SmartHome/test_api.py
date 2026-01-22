import requests
import json

BASE_URL = "http://localhost:5000"

if __name__ == "__main__":
    headers = {"Content-type": "application/json", "Accept": "application/json"}

    serial = "SN-TEST-001"

    # 1) GET /
    response = requests.get(f"{BASE_URL}/", headers=headers)
    print("\nGET /")
    print(response.status_code, response.json())

    # 2) GET /devices
    response = requests.get(f"{BASE_URL}/devices", headers=headers)
    print("\nGET /devices")
    print(response.status_code, response.json())

    # 3) POST /devices
    new_device = {
        "type": "bulb",
        "serial_number": serial,
        "brand": "TestBrand",
        "room": "Bedroom",
        "installation_year": 2024,
        "status": "online",
        "brightness_lumens": 800,
        "color_capability": True,
    }

    response = requests.post(f"{BASE_URL}/devices", headers=headers, json=new_device)
    print("\nPOST /devices")
    print(response.status_code, response.json())

    # 4) GET /devices/<serial>
    response = requests.get(f"{BASE_URL}/devices/{serial}", headers=headers)
    print(f"\nGET /devices/{serial}")
    print(response.status_code, response.json())

    # 5) PATCH /devices/<serial>/status
    patch_data = {"status": "offline"}

    response = requests.patch(
        f"{BASE_URL}/devices/{serial}/status", headers=headers, json=patch_data
    )
    print(f"\nPATCH /devices/{serial}/status")
    print(response.status_code, response.json())

    # 6) PUT /devices/<serial>
    put_data = {
        "type": "bulb",
        "serial_number": serial,
        "brand": "UpdatedBrand",
        "room": "Living Room",
        "installation_year": 2025,
        "status": "online",
        "brightness_lumens": 1200,
        "color_capability": False,
    }

    response = requests.put(
        f"{BASE_URL}/devices/{serial}", headers=headers, json=put_data
    )
    print(f"\nPUT /devices/{serial}")
    print(response.status_code, response.json())

    # 7) DELETE /devices/<serial>
    response = requests.delete(f"{BASE_URL}/devices/{serial}", headers=headers)
    print(f"\nDELETE /devices/{serial}")
    print(response.status_code, response.json())

    # 8) GET /devices/<serial> (deve dare 404)
    response = requests.get(f"{BASE_URL}/devices/{serial}", headers=headers)
    print(f"\nGET dopo DELETE /devices/{serial}")
    print(response.status_code, response.json())