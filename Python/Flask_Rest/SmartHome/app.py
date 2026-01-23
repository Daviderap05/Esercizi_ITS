from flask import Flask, url_for, jsonify, request
from Class.SmartBulb import SmartBulb
from Class.SecurityCamera import SecurityCamera
from classMain import hub


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "message": "Smart Home Hub API",
            "links": {
                "device_list": url_for("list_devices"),
                "bulb_sample": url_for("get_device", serial_number="SN-101"),
                "camera_sample": url_for("get_device", serial_number="SN-10293-X"),
                "estimate_bulb_sample": url_for(
                    "device_diagnostic", serial_number="SN-101", factor=1.0
                ),
                "estimate_camera_sample": url_for(
                    "device_diagnostic", serial_number="SN-10293-X", factor=2.0
                ),
            },
        }
    )


@app.route("/devices", methods=["GET"])
def list_devices():
    return jsonify(hub.list_all())


@app.route("/devices/<string:serial_number>", methods=["GET"])
def get_device(serial_number: str):
    device = hub.get(serial_number)

    if device is None:
        return jsonify({"error": "device not found"}), 404

    return jsonify(device.info())   


@app.route("/devices/<string:serial_number>/diagnostic/<float:factor>", methods=["GET"])
def device_diagnostic(serial_number: str, factor: float):
    device = hub.get(serial_number)

    if device is None:
        return jsonify({"error": "device not found"}), 404

    return jsonify(
        {
            "serial_number": serial_number,
            "device_type": device.device_type(),
            "factor": factor,
            "diagnostic_seconds": device.diagnostics_time(factor),
        }
    )


@app.route("/devices", methods=["POST"])
def add():
    data: dict = request.get_json()

    # 1) body presente (POST = dati nel JSON)
    if data is None:
        return jsonify({"error": "Missing JSON body"}), 400

    # 2) tipo dispositivo valido (serve per sapere che classe creare)
    device_type: str | None = data.get("type")

    if device_type not in ("bulb", "camera"):
        return (
            jsonify(
                {"error": "Invalid or missing 'type'. Must be 'bulb' or 'camera'."}
            ),
            400,
        )

    # 3) campi comuni obbligatori per TUTTI i device
    required_common: list[str] = [
        "serial_number",
        "brand",
        "room",
        "installation_year",
        "status",
    ]

    # 4) campi specifici in base al tipo (bulb / camera)
    if device_type == "bulb":
        required_specific: list[str] = ["brightness_lumens", "color_capability"]
    else:
        required_specific: list[str] = ["resolution", "night_vision"]

    # 5) controllo che NON manchi nessun campo (POST = dati completi)
    missing: list[str] = [
        field for field in (required_common + required_specific) if field not in data
    ]

    if missing:
        return (
            jsonify(
                {
                    "error": "Missing required fields",
                    "missing": missing,
                }
            ),
            400,
        )

    # 6) controllo che l'ID NON esista già (POST = creazione nuova risorsa)
    device_id: str = data["serial_number"]

    if hub.get(device_id) is not None:
        return (
            jsonify({"error": f"device with id '{device_id}' already exists"}),
            400,
        )

    # 7) creazione dell’oggetto corretto in base al tipo
    if device_type == "bulb":
        device: SmartBulb = SmartBulb(
            serial_number=data["serial_number"],
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            brightness_lumens=data["brightness_lumens"],
            color_capability=data["color_capability"],
            power_watt=data.get("power_watt", 9),
        )
    else:
        device: SecurityCamera = SecurityCamera(
            serial_number=data["serial_number"],
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            resolution=data["resolution"],
            night_vision=data["night_vision"],
            power_watt=data.get("power_watt", 50),
        )

    # 8) inserimento nel sistema (collezione devices)
    hub.add(device)

    # 9) risposta: risorsa creata → 201 Created
    return (
        jsonify(
            {
                "status": "ok",
                "added": {
                    "serial_number": device_id,
                    "type": device_type,
                },
            }
        ),
        201,  # Created
    )


@app.route("/devices/<string:serial_number>", methods=["PUT"])
def put(serial_number: str):
    data: dict = request.get_json()

    # 1) body presente
    if data is None:
        return jsonify({"error": "Missing JSON body"}), 400

    # 2) risorsa deve esistere (PUT = sostituzione)
    if hub.get(serial_number) is None:
        return (
            jsonify({"error": f"device with id '{serial_number}' not exists"}),
            404,
        )

    # 3) coerenza ID URL vs body
    if data.get("serial_number") != serial_number:
        return jsonify({"error": "serial_number mismatch"}), 400

    # 4) tipo valido
    device_type: str | None = data.get("type")

    if device_type not in ("bulb", "camera"):
        return (
            jsonify(
                {"error": "Invalid or missing 'type'. Must be 'bulb' or 'camera'."}
            ),
            400,
        )

    # 5) campi obbligatori (PUT = tutti)
    required_common: list[str] = [
        "serial_number",
        "brand",
        "room",
        "installation_year",
        "status",
    ]

    if device_type == "bulb":
        required_specific: list[str] = ["brightness_lumens", "color_capability"]
    else:
        required_specific: list[str] = ["resolution", "night_vision"]

    missing: list[str] = [
        field for field in (required_common + required_specific) if field not in data
    ]

    if missing:
        return (
            jsonify(
                {
                    "error": "Missing required fields",
                    "missing": missing,
                }
            ),
            400,
        )

    # 6) creazione nuovo oggetto (sostituzione totale)
    if device_type == "bulb":
        device: SmartBulb = SmartBulb(
            serial_number=data["serial_number"],
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            brightness_lumens=data["brightness_lumens"],
            color_capability=data["color_capability"],
            power_watt=data.get("power_watt", 9),
        )
    else:
        device: SecurityCamera = SecurityCamera(
            serial_number=data["serial_number"],
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            resolution=data["resolution"],
            night_vision=data["night_vision"],
            power_watt=data.get("power_watt", 50),
        )

    # 7) sostituzione nel sistema
    hub.update(serial_number, device)

    # 8) risposta: risorsa aggiornata → 200 Updated
    return (
        jsonify(
            {
                "status": "ok",
                "updated": {
                    "serial_number": serial_number,
                    "type": device_type,
                },
            }
        ),
        200,  # Updated
    )


@app.route("/devices/<string:serial_number>/status", methods=["PATCH"])
def patch(serial_number: str):
    data: dict = request.get_json()

    # 1) body presente (PATCH = dati nel JSON)
    if data is None:
        return jsonify({"error": "Missing JSON body"}), 400

    # 2) device deve esistere
    if hub.get(serial_number) is None:
        return (
            jsonify({"error": f"device with id '{serial_number}' not exists"}),
            404,
        )

    # 3) deve esserci SOLO il campo che vogliamo aggiornare: status
    if "status" not in data:
        return jsonify({"error": "Missing field 'status'"}), 400

    # (opzionale ma ottimo) controllo valori ammessi
    if data["status"] not in ("online", "offline", "updating", "error"):
        return jsonify({"error": "Invalid status value"}), 400

    # 4) aggiornamento parziale (PATCH)
    hub.patch_status(serial_number, data["status"])

    # 5) risposta OK
    return (
        jsonify(
            {
                "status": "ok",
                "updated": {
                    "serial_number": serial_number,
                    "status": data["status"],
                },
            }
        ),
        200,
    )


@app.route("/devices/<string:serial_number>", methods=["DELETE"])
def delete(serial_number: str):
    # 1) device deve esistere
    if hub.get(serial_number) is None:
        return (
            jsonify({"error": f"device with id '{serial_number}' not exists"}),
            404,
        )

    # 2) rimozione dal sistema
    hub.delete(serial_number)

    # 3) risposta OK
    return (
        jsonify(
            {
                "status": "ok",
                "deleted": {"serial_number": serial_number},
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
