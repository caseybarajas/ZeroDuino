from flask import Flask, render_template, jsonify
import serial
import threading

app = Flask(__name__)
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.flush()

data = {"counter": 0}

def read_from_arduino():
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            data["counter"] = line

thread = threading.Thread(target=read_from_arduino)
thread.start()

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/data')
def data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
