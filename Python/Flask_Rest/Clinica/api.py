from flask import Flask, url_for, jsonify, request
from main import hub
from Class.medical_visit import MedicalVisit
from Class.diagnostic_exam import DiagnosticExam


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        {
            "description": "description",
            "links": {
                "a": url_for("bookings_list"),
                "b": url_for("get_booking", booking_id="BK-VISIT-001"),
                "c": url_for("get_booking", booking_id="BK-EXAM-999"),
                "d": url_for("wait", booking_id="BK-VISIT-001", factor=1.0),
                "e": url_for("wait", booking_id="BK-EXAM-999", factor=2.0),
            },
        }
    )


@app.route("/bookings")
def bookings_list():
    return jsonify(hub.list_all())


@app.route("/bookings/<string:booking_id>")
def get_booking(booking_id: str):
    a = hub.get(booking_id)

    if a is None:
        return jsonify({"error": "error"}), 404

    return jsonify(a.info())


@app.route("/bookings/<string:booking_id>/wait/<float:factor>")
def wait(booking_id: str, factor: float):
    a = hub.get(booking_id)

    if a is None:
        return jsonify({"error": "error"}), 404

    return jsonify({"await": a.estimated_wait(factor)})


@app.route("/bookings", methods=["POST"])
def post():
    # -------------------------------------------------
    data: dict = request.get_json()
    if data is None:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    booking_id: str | None = data.get("booking_id")
    if hub.get(booking_id) is not None:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    booking_type: str = data.get("type")

    # -------------------------------------------------
    # -------------------------------------------------
    campi_comuni: list[str] = [
        "type",
        "booking_id",
        "patient_name",
        "doctor",
        "department",
        "date",
        "time",
        "status",
    ]

    if booking_type == "visit":
        campi_specifici: list[str] = ["visit_reason", "first_time"]
    else:
        campi_specifici: list[str] = ["exam_type", "requires_fasting"]

    campi_mancanti: list[str] = [
        campi for campi in (campi_comuni + campi_specifici) if campi not in data
    ]

    if campi_mancanti:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    if booking_type == "visit":
        booking: MedicalVisit = MedicalVisit(
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            visit_reason=data["visit_reason"],
            first_time=data["first_time"],
        )
    else:
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            exam_type=data["exam_type"],
            requires_fasting=data["requires_fasting"],
        )
    # -------------------------------------------------
    # -------------------------------------------------
    hub.add(booking)
    # -------------------------------------------------
    # -------------------------------------------------
    return jsonify({"Created": "ok", "info": booking.info()}), 201


@app.route("/bookings/<string:booking_id>", methods=["PUT"])
def put(booking_id: str):
    # -------------------------------------------------
    data: dict = request.get_json()
    if data is None:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    if hub.get(booking_id) is None:
        return jsonify({"error": "error"}), 404

    if data.get("booking_id") != booking_id:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    booking_type: str = data.get("type")
    if booking_type not in ("visit", "exam"):
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    campi_comuni: list[str] = [
        "type",
        "booking_id",
        "patient_name",
        "doctor",
        "department",
        "date",
        "time",
        "status",
    ]

    if booking_type == "visit":
        campi_specifici: list[str] = ["visit_reason", "first_time"]
    else:
        campi_specifici: list[str] = ["exam_type", "requires_fasting"]

    campi_mancanti: list[str] = [
        campi for campi in (campi_comuni + campi_specifici) if campi not in data
    ]

    if campi_mancanti:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    if booking_type == "visit":
        booking: MedicalVisit = MedicalVisit(
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            visit_reason=data["visit_reason"],
            first_time=data["first_time"],
        )
    else:
        booking: DiagnosticExam = DiagnosticExam(
            booking_id=data["booking_id"],
            patient_name=data["patient_name"],
            doctor=data["doctor"],
            department=data["department"],
            date=data["date"],
            time=data["time"],
            status=data["status"],
            exam_type=data["exam_type"],
            requires_fasting=data["requires_fasting"],
        )
    # -------------------------------------------------
    # -------------------------------------------------
    hub.update(booking_id, booking)
    # -------------------------------------------------
    # -------------------------------------------------
    return jsonify({"Updated": "ok", "info": booking.info()}), 200


@app.route("/bookings/<string:booking_id>/status", methods=["PATCH"])
def patch(booking_id: str):
    data: dict = request.get_json()
    if data is None:
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    if hub.get(booking_id) is None:
        return jsonify({"error": "error"}), 404
    # -------------------------------------------------
    # -------------------------------------------------
    if data.get("status") is None:
        return jsonify({"error": "error"}), 400

    if data.get("status") not in (
        "scheduled",
        "checked_in",
        "completed",
        "canceled",
        "no_show",
    ):
        return jsonify({"error": "error"}), 400
    # -------------------------------------------------
    # -------------------------------------------------
    hub.patch_status(booking_id, data.get("status"))
    # -------------------------------------------------
    # -------------------------------------------------
    return jsonify({"Updated": "ok"}), 200


@app.route("/bookings/<string:booking_id>", methods=["DELETE"])
def delete(booking_id: str):
    if hub.get(booking_id) is None:
        return jsonify({"error": "error"}), 404
    # -------------------------------------------------
    # -------------------------------------------------
    hub.delete(booking_id)
    # -------------------------------------------------
    # -------------------------------------------------
    return jsonify({"Deleted": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True)
