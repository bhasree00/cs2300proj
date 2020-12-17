from flask import render_template, request
from app import app, db, models
from app.forms import NewPatientForm, NewSurgeryForm
from flask import render_template, flash, redirect
from app.models import Patient, Surgery

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')

#git status test

@app.route('/add_patient', methods=['GET', 'POST'])
def addPatient():
    form = NewPatientForm()
    #if form.validate_on_submit() and not Patient.query.get(form.patientID.data):
    p = Patient(patientID = form.patientID.data, name = form.name.data, preExistCond = form.preExistCond.data, age = form.age.data, gender = form.gender.data, healthInsurance = form.healthInsurance.data)
    db.session.add(p)
    db.session.commit()
    print("Added Patient", form.name.data)
    print("Patient ID:", form.patientID.data)
    print("Pre-Existing Condition:", form.preExistCond.data)
    print("Age:", form.age.data)
    print("Gender:", form.gender.data)
    print("Health Insurance:", form.healthInsurance.data)
    return render_template('addPatient.html', title="Admit Patient", form=form)
    #elif Patient.query.get(form.patientID.data):
        #print("This patient already exists as", form.name.data)
        #return render_template('addPatient.html', title="Admit Patient", form=form, error="EXISTING PATIENT ID ERROR")

    return render_template("index.html", title="Home")

@app.route('/create_surgery', methods=['GET', 'POST'])
def addSurgery():
    return render_template("addSurgery.html", title="Create Surgery")