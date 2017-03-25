import requests
import indicoio
import os
import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError
from wtforms.validators import DataRequired

indicoio.config.api_key = '426cd40e597f61242dba879063d99567'

def get_emotion(string):
	user_input = input("What are you thinking about right now?")
	print "Ok, you're thinking about " + str(user_input)
	emotion = indicoio.emotion(user_input)
	print emotion


class MyForm(FlaskForm):
    name = StringField('Your name:', validators=[DataRequired()])

class EmotionForm(FlaskForm):
	text = StringField('Get your emotion:', validators=[DataRequired()])





app = Flask(__name__)
app.secret_key = 'demo1234!'
bootstrap = Bootstrap(app)
login_manager = flask_login.LoginManager()

login_manager.init_app(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success')
def success():
    return 'Success! Waiting for other players to join.'

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0',port=port)