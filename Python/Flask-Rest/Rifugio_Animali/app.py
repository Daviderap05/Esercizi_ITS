from flask import Flask, url_for, jsonify
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

    if shelter.is_adoptded(animal_id):
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

if __name__ == "__main__":
    app.run(debug=True)