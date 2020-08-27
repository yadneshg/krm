import base64
import functools
import flask
from app import *
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename
from base64 import b64encode

from utility.image_utility import resize_image
from utility.image_utility import allowed_file

bp_employee = Blueprint('employee', __name__, url_prefix='/employee')

app = Flask(__name__)
@bp_employee.route("/employees")
def employees():
    employees = Employee_master.query.all()
    print(employees)
    for employee in employees:
        print(employee.is_active)
    units=Unit_master.query.all()
    print(units)
    return render_template('employee/employees.html', employees=employees, units=units)

@bp_employee.route("/employeedetails/<employee_id>")
def employeedetails(employee_id):
    employee = Employee_master.query.get(employee_id)
    employee_unit = Unit_master.query.get(employee.unit_id)
    units=Unit_master.query.all()
    image = base64.b64encode(employee.photo_id).decode("ascii")
    # return render_template('employee/employeedetails.html', image=image)
    if employee.is_active == True:
        return render_template('employee/employeedetails.html', employee=employee, employee_unit=employee_unit, units=units, image=image)
    else:
        return render_template("index.html", message="No Such Unit.")


@bp_employee.route("/add_employee", methods=['GET', 'POST'])
def add_employee():
    firstname = request.form.get("first_name")
    middlename = request.form.get("middle_name")
    lastname = request.form.get("last_name")
    birthdate= request.form.get("birth_date")
    employeeaddress = request.form.get("employee_address")
    mobile = request.form.get("mobile")
    gender = request.form.get("gender")
    unitid = request.form.get("employee_unit")
    joining_date = request.form.get("joining_date")
    joiningdate = dt.datetime.strptime(joining_date, '%Y-%m-%d')
    designation = request.form.get("designation")
    photoidno = request.form.get("photo_id_no")
    photoid = request.files.get("photo_id")

    image = secure_filename(photoid.filename)
    if allowed_file(image):
        print(allowed_file(image))
    photoid_data = resize_image(image=photoid, width=500, height=500, max_allowed_size=3, need_to_resize=1)

    employee = Employee_master(
        first_name=firstname,
        middle_name=middlename,
        last_name=lastname,
        birth_date=birthdate,
        address=employeeaddress,
        mobile=mobile,
        gender=gender,
        unit_id=unitid,
        joining_date=joiningdate,
        designation=designation,
        photo_id_no=photoidno,
        photo_id=photoid_data,
        is_active=True,
    )
    if employee is None:
        # message = "No Such Unit."
        return redirect('url_for("employee.employees")')
    try:
        db.session.commit()
        message = "Employee Details Edited"
    except TypeError:
        db.session.rollback()
        message = "Error in db"
    db.session.add(employee)
    db.session.commit()
    employees = Employee_master.query.all()
    message = "Employee Added"
    return render_template('employee/employees.html', employees=employees, message=message)


@bp_employee.route("/edit_employee/<employee_id>", methods=['GET', 'POST'])
def edit_employee(employee_id):
    # firstname = request.form.get("first_name")
    # middlename = request.form.get("middle_name")
    # lastname = request.form.get("last_name")
    # birthdate= request.form.get("birth_date")
    employeeaddress = request.form.get("employee_address")
    mobile = request.form.get("mobile")
    # joining_date = request.form.get("joining_date")
    # joiningdate = dt.datetime.strptime(joining_date, '%Y-%m-%d')
    employeeunit = request.form.get("employee_unit")
    designation = request.form.get("designation")
    photoidno = request.form.get("photo_id_no")
    photoid = request.files.get("photo_id")

    image = secure_filename(photoid.filename)
    if allowed_file(image):
        print(allowed_file(image))
    photoid_data = resize_image(image=photoid, width=500, height=500, max_allowed_size=3, need_to_resize=1)

    employee = Employee_master.query.get(employee_id)
    if employee is not None:
        employee.address = employeeaddress
        employee.mobile = mobile
        employee.employee_unit = employeeunit
        employee.designation = designation
        employee.photo_id_no = photoidno
        employee.photo_id = photoid_data
        print(employee.mobile)
        try:
            db.session.commit()
            message = "Employee Details Edited"
        except TypeError:
            db.session.rollback()
            message = "Error in db"
    else:
        message = "Error"
    employees = Employee_master.query.all()
    return render_template('employee/employees.html', employees=employees, message=message)


@bp_employee.route("/disable_employee/<employee_id>", methods=['GET', 'POST'])
def disable_employee(employee_id):
    isworking = request.form.get("is_working")
    print(isworking)
    # is_working = True
    message = None
    if isworking == "False":
        is_working = False
        print(is_working)
        employee = Employee_master.query.get(employee_id)
        if employee is not None:
            employee.is_active = is_working
            db.session.commit()
            message = "Employee Removed"
    else:
        message = "No Action Taken!"
    employees = Employee_master.query.all()
    return render_template('employee/employees.html', employees=employees, message=message)

@bp_employee.route('/display_photo_id/<int:photo_id>', methods=['GET'])
def display_photo_id(photo_id):
    print(photo_id)
    photoid = Employee_master.query.get(photo_id)
    photo_id_display = photoid.photo_id
    return app.response_class(photo_id_display)