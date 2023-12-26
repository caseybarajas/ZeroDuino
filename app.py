from flask import Flask, render_template, request
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_text', methods=['POST'])
def send_text():
    text = request.form['text']
    ser.write(text.encode())  # Send the text to the Arduino
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
