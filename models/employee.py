from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__="tblemployees"

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    salary=db.Column(db.Integer)
