from flask_wtf import FlaskForm
from wtforms import BooleanField, Form, TextField, TextAreaField, validators, StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired

#class LoginForm(Form):
#    openid = StringField('openid', validators=[DataRequired()])
#    remember_me = BooleanField('remember_me', default=False)

class NewPatientForm(FlaskForm):
    patientID = IntegerField('patientID', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    preExistCond = StringField('preExistCond', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired()])
    gender = StringField('gender', validators=[DataRequired()])
    healthInsurance = StringField('healthInsurance', validators=[DataRequired()])

class NewSurgeryForm(FlaskForm):
    surgeryID = IntegerField('surgeryID', validators=[DataRequired()])
    mortalityRate = FloatField('mortalityRate', validators=[DataRequired()])
    typeOf = StringField('typeOf', validators=[DataRequired()])
    cost = FloatField('cost', validators=[DataRequired()])