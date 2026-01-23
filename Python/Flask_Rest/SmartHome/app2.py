from flask import Flask, url_for, request, jsonify
from Class.SmartBulb import SmartBulb
from Class.SecurityCamera import SecurityCamera
from classMain import hub


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "message": "messaggio",
            "links": {
                "lista_device": url_for("device_lista"),
                "device_sample_bulb": url_for("get_device", serial_number="SN-101"),
                "device_sample_camera": url_for(
                    "get_device", serial_number="SN-10293-X"
                ),
                "diagnostic_time_bulb": url_for(
                    "diagnostics_time", serial_number="SN-101", factor=1.0
                ),
                "diagnostic_time_camera": url_for(
                    "diagnostics_time", serial_number="SN-10293-X", factor=2.0
                ),
            },
        }
    )


@app.route("/devices", methods=["GET"])
def device_lista():
    return jsonify(hub.list_all())


@app.route("/devices/<string:serial_number>", methods=["GET"])
def get_device(serial_number: str):
    device = hub.get(serial_number)

    if device is None:
        return jsonify({"error": "error"}), 404

    return jsonify(device.info())


@app.route("/devices/<string:serial_number>/diagnostic/<float:factor>", methods=["GET"])
def diagnostics_time(serial_number: str, factor: float):
    device = hub.get(serial_number)

    if device is None:
        return jsonify({"error": "error"}), 404

    return jsonify({"diagnostic_time": device.diagnostics_time(factor)})


@app.route("/devices", methods=["POST"])
def post():
    data: dict = request.get_json()

    if data is None:
        return jsonify({"error": "error"}), 400

    # controllo che l'id non esista già
    device_id = data["serial_number"]

    if hub.get(device_id) is not None:
        return jsonify({"error": "error"}), 400

    device_type: str | None = data.get("type")

    if device_type not in ("bulb", "camera"):
        return jsonify({"error": "error"}), 400

    campi_comuni: list[str] = [
        "serial_number",
        "brand",
        "room",
        "installation_year",
        "status",
    ]

    if device_type == "bulb":
        campi_specifici: list[str] = [
            "brightness_lumens",
            "color_capability",
        ]
    else:
        campi_specifici: list[str] = [
            "resolution",
            "night_vision",
        ]

    campi_mancanti: list[str] = [
        campi for campi in (campi_comuni + campi_specifici) if campi not in data
    ]

    if campi_mancanti:
        return jsonify({"error": "error"}), 400

    # creazione oggetto
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

    hub.add(device)

    return jsonify({"Created": "ok"}), 201


@app.route("/devices/<string:serial_number>", methods=["PUT"])
def put(serial_number: str):
    data: dict = request.get_json()

    if data is None:
        return jsonify({"error": "error"}), 400

    # ciò che cambia:
    # -------------------------------------------

    if hub.get(serial_number) is None:
        return jsonify({"error": "error"}), 404

    if data.get("serial_number") != serial_number:
        return jsonify({"error": "error"}), 400

    # ------------------------------------------

    device_type: str | None = data.get("type")

    if device_type not in ("bulb", "camera"):
        return jsonify({"error": "error"}), 400

    campi_comuni: list[str] = [
        "serial_number",
        "brand",
        "room",
        "installation_year",
        "status",
    ]

    if device_type == "bulb":
        campi_specifici: list[str] = [
            "brightness_lumens",
            "color_capability",
        ]
    else:
        campi_specifici: list[str] = [
            "resolution",
            "night_vision",
        ]

    campi_mancanti: list[str] = [
        campi for campi in (campi_comuni + campi_specifici) if campi not in data
    ]

    if campi_mancanti:
        return jsonify({"error": "error"}), 400

    # creazione oggetto
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

    hub.update(serial_number, device)

    return jsonify({"Updated": "ok"}), 200


@app.route("/devices/<string:serial_number>/status", methods=["PATCH"])
def patch(serial_number: str):
    data: dict = request.get_json()

    if data is None:
        return jsonify({"error": "error"}), 400

    if hub.get(serial_number) is None:
        return jsonify({"error": "error"}), 404

    # ciò che cambia --> non serve creare un oggetto, bisogna solo controllare il campo:
    # ------------------------------------------------------------------
    if "status" not in data:
        return jsonify({"error": "error"}), 400

    if data["status"] not in ("online", "offline", "updating", "error"):
        return jsonify({"error": "error"}), 400
    # ------------------------------------------------------------------

    hub.patch_status(serial_number, data["status"])

    return jsonify({"Updated": "ok"}), 200


@app.route("/devices/<string:serial_number>", methods=["DELETE"])
def delete(serial_number: str):
    if hub.get(serial_number) is None:
        return jsonify({"error": "error"}), 404

    hub.delete(serial_number)

    return jsonify({"Deleted": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True)
