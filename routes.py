from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO

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
            print 'right pressed'
        elif request.form['btn'] == 'left':
            print 'left pressed'
        elif request.form['btn'] == 'down':
            print 'down pressed'
        elif request.form['btn'] == 'up':
            print 'up pressed'

    return redirect(url_for('home'))

@app.route('/hello/<name>/<int:age>/<float:weight>')
def hello(name, age, weight):
    return "Hello, {} your age is {} and you weight {}".format(name, age, weight)

if __name__ == '__main__':
    socketio.run(app, debug=True)