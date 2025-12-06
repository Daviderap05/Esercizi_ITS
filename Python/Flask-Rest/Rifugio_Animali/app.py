from flask import Flask, url_for, jsonify, request
from Class.Dog import Dog
from Class.Cat import Cat
from classMain import shelter


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "message": "Welcome to Animal Shelter API",
            "links": {
                "animals": url_for("list_animals"),
                "sample_dog": url_for("get_animal", animal_id="d1"),
                "sample_cat": url_for("get_animal", animal_id="c1"),
                "food_requiremtents_d1": url_for(
                    "animal_food_requirements", animal_id="d1"
                ),
                "food_requiremtents_c1": url_for(
                    "animal_food_requirements", animal_id="c1"
                ),
                "adoption_d1": url_for("animal_adoption", animal_id="d1"),
                "adoption_c1": url_for("animal_adoption", animal_id="c1"),
            },
        }
    )


@app.route("/animals", methods=["GET"])
def list_animals():
    return jsonify(shelter.list_all())


@app.route("/animals/<string:animal_id>", methods=["GET"])
def get_animal(animal_id: str):
    animal = shelter.get(animal_id)

    if animal is None:
        return jsonify({"error": "Animal not found"}), 404
    return jsonify(animal.info())


@app.route("/animals/<string:animal_id>/food", methods=["GET"])
def animal_food_requirements(animal_id: str):
    animal = shelter.get(animal_id)

    if animal is None:
        return jsonify({"error": "Animal not found"}), 404

    return jsonify(
        {
            "animal_id": animal_id,
            "daily_food_grams": animal.daily_food_grams(),
        }
    )


@app.route("/animals/<string:animal_id>/adoption", methods=["GET"])
def animal_adoption(animal_id: str):
    animal = shelter.get(animal_id)

    if animal is None:
        return jsonify({"error": "Animal not found"}), 404

    if shelter.is_adopted(animal_id):
        return jsonify(
            {
                "animal_id": animal_id,
                "adopted": True,
                "adopter_name": shelter.get_name_adopter(animal_id),
            }
        )
    else:
        return jsonify(
            {
                "animal_id": animal_id,
                "adopted": False,
            }
        )


@app.route("/animals/add", methods=["POST"])
def add_animal():
    data: dict = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    animal_type: str | None = data.get("type")

    if animal_type not in ("dog", "cat"):
        return (
            jsonify({"error": "Invalid or missing 'type'. Must be 'dog' or 'cat'."}),
            400,
        )

    # campi comuni
    required_common: list[str] = ["id", "name", "age_years", "weight_kg"]

    # campi specifici
    if animal_type == "dog":
        required_specific: list[str] = ["breed", "is_trained"]
    else:  # cat
        required_specific: list[str] = ["indoor_only", "favorite_toy"]

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

    animal_id: str = data["id"]

    # controllo se esiste già
    if shelter.get(animal_id) is not None:
        return (
            jsonify({"error": f"Animal with id '{animal_id}' already exists"}),
            400,
        )

    # creazione istanza
    if animal_type == "dog":
        new_animal: Dog = Dog(
            id=animal_id,
            name=data["name"],
            age_years=data["age_years"],
            weight_kg=data["weight_kg"],
            breed=data["breed"],
            is_trained=data["is_trained"],
        )
    else:  # cat
        new_animal: Cat = Cat(
            id=animal_id,
            name=data["name"],
            age_years=data["age_years"],
            weight_kg=data["weight_kg"],
            indoor_only=data["indoor_only"],
            favorite_toy=data["favorite_toy"],
        )

    shelter.add(new_animal)

    return (
        jsonify(
            {
                "status": "ok",
                "added": {
                    "id": animal_id,
                    "species": animal_type,
                },
            }
        ),
        201,  # Created
    )


@app.route("/animals/<string:animal_id>/adopt", methods=["POST"])
def adopt_animal(animal_id: str):
    animal = shelter.get(animal_id)

    if animal is None:
        return jsonify({"error": "Animal not found"}), 404

    # se è già adottato (usa lo stesso metodo che usi nella GET)
    if shelter.is_adopted(animal_id):
        return (
            jsonify(
                {
                    "error": "Animal already adopted",
                    "id": animal_id,
                    "adopter_name": shelter.get_name_adopter(animal_id),
                }
            ),
            400,
        )

    data = request.get_json()
    if not data or "adopter_name" not in data:
        return jsonify({"error": "Missing field 'adopter_name' in JSON body"}), 400

    adopter_name = data["adopter_name"]

    shelter.set_adopted(animal_id, adopter_name)

    return jsonify(
        {
            "id": animal_id,
            "adopted": True,
            "adopter_name": adopter_name,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
