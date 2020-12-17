from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
#from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange
from datetime import date

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models