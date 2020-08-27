
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class Unit_master(db.Model):
    __tablename__ = "unit_master"
    id = db.Column(db.Integer, primary_key=True)
    unit_name=db.Column(db.String(50), nullable=False)
    address=db.Column(db.String(355))
    phone=db.Column(db.Unicode(255), nullable=False)
    starting_date = db.Column(db.DateTime)
    closing_date = db.Column(db.DateTime)
    description=db.Column(db.String(355))
    is_active = db.Column(db.Boolean(), default=True)

class Employee_master(db.Model):
    __tablename__ = "employee_master"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.DateTime)
    address = db.Column(db.String(355))
    mobile = db.Column(db.Unicode(255), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    unit_id=db.Column(db.Integer, ForeignKey("unit_master.id"), nullable=False)
    joining_date = db.Column(db.DateTime)
    leaving_date = db.Column(db.DateTime)
    designation = db.Column(db.String(20))
    photo_id_no = db.Column(db.String(20))
    photo_id = db.Column(db.LargeBinary)
    is_active = db.Column(db.Boolean(), default=True)


class Salary_master(db.Model):
    __tablename__ = "salary_master"
    id = db.Column(db.Integer, primary_key=True)
    emp_id=db.Column(db.Integer, ForeignKey("employee_master.id"), nullable=False)
    salary=db.Column(db.Integer, nullable=False)
    effective_date = db.Column(db.TIMESTAMP, nullable=False)

class Account_category(db.Model):
    __tablename__ = "account_category"
    id = db.Column(db.Integer, primary_key=True)
    category=db.Column(db.String(100), nullable=False)
    type=db.Column(db.String(20), nullable=False)


#     lastname = db.Column(db.String, nullable=False)
#     email=db.Column(db.String(355))
#     mobile=db.Column(db.Unicode(255), nullable=False)
#     dob=db.Column(db.DateTime)
#     strava_id= db.Column(db.Integer)
#     t_size=db.Column(db.Integer)
#     t_number=db.Column(db.Integer)
#     username = db.Column(db.String(), nullable=False)
#     password = db.Column(db.String(), nullable=False)
#     profilepic = db.Column(db.LargeBinary)
#
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(), nullable=False)
#     password=db.Column(db.String(),nullable=False )
#     firstname=db.Column(db.String, nullable=False)
#     lastname = db.Column(db.String, nullable=False)
#     email=db.Column(db.String(355))
#     mobile=db.Column(db.Unicode(255), nullable=False)
#
# class Blogpost(db.Model):
#     __tablename__ = "blogposts"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
#     author = db.Column(db.String(20))
#     date_posted = db.Column(db.DateTime)
#     content = db.Column(db.Text)
#
# class Event(db.Model):
#     __tablename__ = "events"
#     id = db.Column(db.Integer, primary_key=True)
#     title=db.Column(db.String(255), nullable=False)
#     start_date=db.Column(db.TIMESTAMP, nullable=False)
#     end_date = db.Column(db.TIMESTAMP, nullable=False)
#     event_description= db.Column(db.String(255), nullable=True)
#
# class Guser(db.Model, UserMixin):
#     __tablename__ = 'gusers'
#     id = db.Column(db.Text, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     email = db.Column(db.String(64), nullable=False, unique=True)
#     profile_pic = db.Column(db.String(255), nullable=True)
#
# class ImageContents(db.Model):
#     __tablename__ = 'image_contents'
#     # __abstract__ = True
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(300))
#     data = db.Column(db.LargeBinary)

