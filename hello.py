import requests
import indicoio
import eventlet
import os
from flask_socketio import SocketIO
from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask import render_template, request, flash, redirect, send_from_directory
from flask_socketio import SocketIO, emit, send

from database.config import db_session
from database.config import get_db, init_db
from database.queries import *

indicoio.config.api_key = '426cd40e597f61242dba879063d99567'

def get_emotion(string):
	user_input = input("What are you thinking about right now?")
	print "Ok, you're thinking about " + str(user_input)
	emotion = indicoio.emotion(user_input)
	print emotion

app = Flask(__name__)
app.secret_key = 'demo1234!'
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/templates/<path:path>')
def send_js(path):
	return send_from_directory('templates', path)

@app.route('/lobby')
def lobby():
	return render_template('lobby.html')

@app.route('/success')
def success():
    return 'Success! Waiting for other players to join.'

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.cli.command('getdb')
def getdb_command():
     """Grabs the db."""
     get_db();
     print('Grabbed the database.')

@app.cli.command('initdb')
def initdb_command():
    """Initializes the db."""
    init_db();
    print('Initialized the database.')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('newUser')
def handle_message(message):
    print("new user");
    emit("response", handle_new_user(message));


if __name__ == '__main__':
	init_db()
	socketio.run(app)
