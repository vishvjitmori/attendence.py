from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    address_name = db.Column(db.String(255), nullable=False)
    street_name = db.Column(db.String(255), nullable=False)
    town = db.Column(db.String(255), nullable=False)
    locality = db.Column(db.String(255), nullable=False)
    post_code = db.Column(db.String(255), nullable=False)
    contact1 = db.Column(db.String(50), nullable=False)
    contact2 = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Employee(db.Model):
    id =  db.Column(db.Integer, primary_key=True, autoincrement=True)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'), nullable=False)
    store = db.relationship('Store', backref='employees') 
    employee_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    designation = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default="active")
    address_name = db.Column(db.String(255), nullable=False)
    street_name = db.Column(db.String(255), nullable=False)
    town = db.Column(db.String(255), nullable=False)
    locality = db.Column(db.String(255), nullable=False)
    post_code = db.Column(db.String(255), nullable=False)
    contact1 = db.Column(db.String(50), nullable=False)
    contact2 = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
