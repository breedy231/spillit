import requests
from flask import Flask
from flask import render_template, request, flash, redirect
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

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



manager = Manager(app)

if __name__ == '__main__':
	manager.run(threaded=True)