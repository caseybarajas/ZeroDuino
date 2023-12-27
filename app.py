from flask import Flask, request, render_template
import serial
import time

app = Flask(__name__)
arduino = serial.Serial('/dev/ttyACM0', 9600)

def send_to_arduino(speed):
    print(f"Sending to Arduino: {speed}")
    arduino.write(f"{speed}\n".encode())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motor', methods=['POST'])
def motor():
    speed = request.form['speed']
    print(f"Received speed: {speed}")
    send_to_arduino(speed)
    return f"Motor set to {speed}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
