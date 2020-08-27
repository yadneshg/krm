from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from app import *

bp_salary = Blueprint('salary', __name__, url_prefix='/salary')

@bp_salary.route("/add_salary")
def add_salary():
    return render_template("salary/add_salary.html")


@bp_salary.route("/salaries")
def salaries():
    salary_details = Salary_master.query.all()
    print(salaries)
    return render_template('salary/salary.html', salary_details=salary_details)