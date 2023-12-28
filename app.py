from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__)

try:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    arduino.flush()
except serial.SerialException as e:
    print("Error opening serial port: ", e)
    exit()

arduino_data = {"counter": 0}

def read_from_arduino():
    while True:
        try:
            if arduino.in_waiting > 0:
                line = arduino.readline().decode('utf-8').rstrip()
                try:
                    # Convert the line to an integer and update the data
                    arduino_data["counter"] = int(line)
                except ValueError:
                    # If the conversion fails, it means the data is not a valid integer
                    print("Invalid data received:", line)
        except serial.SerialException as e:
            print("Error reading from serial port: ", e)
            time.sleep(2)  # Wait for a bit before trying again


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
