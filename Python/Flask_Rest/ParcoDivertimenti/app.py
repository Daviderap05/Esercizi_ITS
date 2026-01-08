from flask import Flask, url_for, jsonify
from classMain import park

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to Park API",
        "links": {
            "rides": url_for('list_rides'),
            "ride_rc1": url_for('ride_detail', ride_id='rc1'),
            "ride_rc1_wait": url_for('ride_wait_time', ride_id='rc1'),
            "ride_rc2": url_for('ride_detail', ride_id='rc2'),
            "ride_rc2_wait": url_for('ride_wait_time', ride_id='rc2')
        }
    })


@app.route('/rides', methods=['GET'])
def list_rides():
    return jsonify(park.list_all())


@app.route('/ride/<string:ride_id>', methods=['GET'])
def ride_detail(ride_id: str):    
    try:
        return jsonify(park.get(ride_id).info())
    
    except AttributeError:
        return jsonify({"error": "Ride not found"}), 404

@app.route('/ride/<string:ride_id>/wait', defaults={'crowd': 1.0}, methods=['GET'])
@app.route('/ride/<string:ride_id>/wait/<float:crowd>', methods=['GET'])
def ride_wait_time(ride_id: str, crowd: float):   
    try:
        ride = park.get(ride_id)
        wait_time = ride.wait_time(crowd)
        return jsonify({
            "ride_id": ride_id,
            "calculated_wait_time_sec": wait_time
        })
        
    except AttributeError:
        return jsonify({"error": "Ride not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)