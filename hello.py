import requests

from flask import Flask, g
from flask import render_template, request, flash, redirect
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

from database.config import db_session
from database.config import get_db, init_db

class MyForm(FlaskForm):
    name = StringField('Your name:', validators=[DataRequired()])

app = Flask(__name__)
app.secret_key = 'demo1234!'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/success')
def success():
    return 'Success! Waiting for other players to join'

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

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

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
