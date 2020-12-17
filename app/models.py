from app import db

class Patient(db.Model):
    __tablename__ = "patient"
    patientID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    preExistCond = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    healthInsurance = db.Column(db.String(1))

    def __repr__(self):
        return '<Patient %r>' % (self.name)



class Surgery(db.Model):
    __tablename__ = "surgery"
    surgeryID = db.Column(db.Integer, primary_key=True)
    mortalityRate = db.Column(db.Float)
    typeOf = db.Column(db.String(80), unique=True)
    cost = db.Column(db.Float)
    surgeriesDoneOn = db.relationship('Undergoes', backref='given', lazy='dynamic')
    conductedBy = db.relationship('Conducts', backref='conductedBy', lazy='dynamic')

    def __repr__(self):
        return '<Surgery Name %r>' % (self.typeOf)



class Department(db.Model):
    __tablename__ = "department"
    deptNumber = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.Float)
    dpName = db.Column(db.String(80), unique=True)
    headDocID = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '<Department %r>' % (self.dpName)



class Doctor(db.Model):
    __tablename__ = "doctor"
    name = db.Column(db.String(80))
    doctorID = db.Column(db.Integer, primary_key=True)
    specialization = db.Column(db.String(80))
    nurses = db.relationship('Nurse', backref='doctor', lazy='dynamic')
    conducting = db.relationship('Conducts', backref='conducting', lazy='dynamic')
    treating = db.relationship('Treats', backref='treating', lazy='dynamic')
    dept = db.relationship('WorksFor', backref='dept', lazy='dynamic')

    def __repr__(self):
        return '<Dr. %r>' % (self.name)



class Nurse(db.Model):
    __tablename__ = "nurse"
    nID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    assignedDoctorID = db.Column(db.Integer, db.ForeignKey('doctor.doctorID'))

    def __repr__(self):
        return '<Nurse %r>' % (self.name)



class Undergoes(db.Model):
    undergoesID = db.Column(db.Integer, primary_key=True)
    sID = db.Column(db.Integer, db.ForeignKey('surgery.surgeryID'))
    pID = db.Column(db.Integer, db.ForeignKey('patient.patientID'))
    testStatement = "sID:" + sID + "\tpID:" + pID

    def __repr__(self):
        return '<Undergoes %r>' % (self.testStatement)



class Conducts(db.Model):
    conductsID = db.Column(db.Integer, primary_key=True)
    sID = db.Column(db.Integer, db.ForeignKey('surgery.surgeryID'))
    dID = db.Column(db.Integer, db.ForeignKey('doctor.doctorID'))
    testStatement = "sID:" + sID + "\tdID:" + dID

    def __repr__(self):
        return '<Conducts %r>' % (self.testStatement)



class Treats(db.Model):
    treatsID = db.Column(db.Integer, primary_key=True)
    pID = db.Column(db.Integer, db.ForeignKey('patient.patientID'))
    dID = db.Column(db.Integer, db.ForeignKey('doctor.doctorID'))
    testStatement = "pID:" + pID + "\tdID:" + dID

    def __repr__(self):
        return '<Treats %r>' % (self.testStatement)



class WorksFor(db.Model):
    worksForID = db.Column(db.Integer, primary_key=True)
    dID = db.Column(db.Integer, db.ForeignKey('doctor.doctorID'))
    dNum = db.Column(db.Integer, db.ForeignKey('department.deptNumber'))
    testStatement = "dID:" + dID + "\tdNum:" + dNum

    def __repr__(self):
        return '<WorksFor %r>' % (self.testStatement)