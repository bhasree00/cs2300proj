from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)

@app.route('/add_patient')
def addPatient():
    return render_template("addPatient.html", title="Admit Patient")

@app.route('/create_surgery')
def addSurgery():
    return render_template("addSurgery.html", title="Create Surgery")