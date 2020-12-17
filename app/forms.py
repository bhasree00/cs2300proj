from flask_wtf import Form, Flask, render_template, flash, request
from wtforms import StringField, BooleanField, Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired

#class LoginForm(Form):
#    openid = StringField('openid', validators=[DataRequired()])
#    remember_me = BooleanField('remember_me', default=False)


class NewPatientForm(FlaskForm):
    patientID = 
    patientID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    preExistCond = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    healthInsurance = db.Column(db.String(1))

