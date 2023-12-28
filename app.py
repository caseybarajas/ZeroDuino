from flask import Flask, render_template, jsonify
import serial
import threading

app = Flask(__name__)
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.flush()

arduino_data = {"counter": 0}  # Renamed variable to avoid conflict

def read_from_arduino():
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            arduino_data["counter"] = line  # Use the renamed variable

thread = threading.Thread(target=read_from_arduino)
thread.start()

@app.route('/')
def index():
    return render_template('index.html', data=arduino_data)  # Pass the renamed variable

@app.route('/data')
def data():
    return jsonify(arduino_data)  # Return the renamed variable as JSON

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
