from flask import Flask, render_template, request
import serial

app = Flask(__name__)

# Set up the serial line (adjust /dev/ttyACM0 to your setting)
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control_led', methods=['POST'])
def control_led():
    action = request.form['action']
    if action == 'on':
        ser.write(b'1')  # Send '1' to Arduino
    elif action == 'off':
        ser.write(b'0')  # Send '0' to Arduino
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
