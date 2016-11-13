from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO
# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(18, GPIO.OUT)

action = {False: 0, True: 1}
state = False

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == "POST":
        if request.form['btn'] == 'right':
            print 'right pressed and action'
            # GPIO.output(17, 1)
        elif request.form['btn'] == 'left':
            print 'left pressed'
            # GPIO.output(17, 0)
        elif request.form['btn'] == 'down':
            print 'down pressed'
        elif request.form['btn'] == 'up':
            print 'up pressed'

    return redirect(url_for('home'))

@app.route('/hello/<name>/<int:age>/<float:weight>')
def hello(name, age, weight):
    return "Hello, {} your age is {} and you weight {}".format(name, age, weight)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')