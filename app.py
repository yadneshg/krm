import os
import datetime as dt
from flask import Flask, render_template, request, redirect
from models import *
import auth
import unit
import employee
import salary

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Cyber123@localhost:5432/krm"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

db.init_app(app)

app.register_blueprint(auth.bp_auth)
app.register_blueprint(unit.bp_unit)
app.register_blueprint(employee.bp_employee)
app.register_blueprint(salary.bp_salary)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')
