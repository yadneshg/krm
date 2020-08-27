import functools
from app import *

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

bp_unit = Blueprint('unit', __name__, url_prefix='/unit')


@bp_unit.route("/units")
def units():
    units = Unit_master.query.all()
    return render_template('unit/units.html', units=units)

@bp_unit.route("/add_unit", methods=['GET', 'POST'])
def add_unit():
    unitname = request.form.get("unit_name")
    unitaddress = request.form.get("unit_address")
    startingdate = request.form.get("starting_date")
    description = request.form.get("description")

    unit = Unit_master(
        unit_name=unitname,
        address=unitaddress,
        starting_date=startingdate,
        description=description,
        is_active=True
    )
    if unit is None:
        return redirect('url_for("units")')
    db.session.add(unit)
    db.session.commit()
    units = Unit_master.query.all()
    message = "Unit Added"
    return render_template('unit/units.html', units=units, message=message)


@bp_unit.route("/edit_unit/<unit_id>", methods=['GET', 'POST'])
def edit_unit(unit_id):
    unitname = request.form.get("unit_name")
    unitaddress = request.form.get("unit_address")
    starting_date = request.form.get("starting_date")
    startingdate = dt.datetime.strptime(starting_date, '%Y-%m-%d')
    description = request.form.get("description")

    unit = Unit_master.query.get(unit_id)
    if unit is not None:
        unit.unit_name = unitname
        unit.address = unitaddress
        unit.starting_date = startingdate
        unit.description = description
        db.session.commit()
        message = "Unit Edited"
    else:
        message = "Error"
    units = Unit_master.query.all()
    return render_template('unit/units.html', units=units, message=message)


@bp_unit.route("/disable_unit/<unit_id>", methods=['GET', 'POST'])
def disable_unit(unit_id):
    isactive = request.form.get("is_active")
    closing_date = request.form.get("closing_date")
    is_active=True
    if isactive == "False":
        is_active = False
    unit = Unit_master.query.get(unit_id)
    if unit is not None and is_active == False:
        unit.is_active = is_active
        unit.closing_date=closing_date
        db.session.commit()
        message = "Unit Removed"
    else:
        message = "Unit Not Removed"
    units = Unit_master.query.all()
    return render_template('unit/units.html', units=units, message=message)


@bp_unit.route("/restart_unit/<unit_id>", methods=['GET', 'POST'])
def restart_unit(unit_id):
    isactive = request.form.get("is_active")
    closing_date = None
    is_active=False
    if isactive == "True":
        is_active = True
    unit = Unit_master.query.get(unit_id)
    if unit is not None and is_active == True:
        unit.is_active = is_active
        unit.closing_date=closing_date
        db.session.commit()
        message = "Unit Restarted"
    else:
        message = "The Unit wil remain dissabled"
    units = Unit_master.query.all()
    return render_template('unit/units.html', units=units, message=message)


@bp_unit.route("/unitdetails/<unit_id>")
def unitdetails(unit_id):
    unit = Unit_master.query.get(unit_id)
    # if unit.is_active == True:
    return render_template('unit/unitdetails.html', unit=unit)
    # else:
    #     return render_template("index.html", message="No Such Unit.")
