
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)




@app.route('/sensor/data', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    print(data)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydb",
        port="3308"
    )

    mycursor = mydb.cursor()

    # {'light': 410.05, 'temperature': 21.57, 'humidity': 99.99}
    for sensors, merijums in data.items():
        print(sensors, merijums)
        sql = "INSERT INTO sensoru_dati (sensora_nosaukums, merijums) VALUES (%s, %s)"
        val = (sensors, merijums)
        mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")




    return jsonify({
        "status": "success",
        "received": data
    }), 200


