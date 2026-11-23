
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sensor/data', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    print(data)

    return jsonify({
        "status": "success",
        "received": data
    }), 200


