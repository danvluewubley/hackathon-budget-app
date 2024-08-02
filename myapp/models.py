from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from . import db



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Stats (db.Model):
    __tablename__ = 'stats'
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    stats_id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Integer)
    deductions = db.Column(db.Integer)
    status = db.Column(db.Integer)
    request = db.relationship("Child", backref=backref("users", uselist=False))

class Savings (db.Model):
    __tablename__ = 'savings'
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    savings_id = db.Column(db.Integer, primary_key=True)
    emergency = db.Column(db.Integer)
    retirement = db.Column(db.Integer)
    debts = db.Column(db.Integer)
    request = db.relationship("Child", backref=backref("users", uselist=False))

class Necessities (db.Model):
    __tablename__ = 'necessities'
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    necessities_id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    groceries = db.Column(db.Integer)
    other = db.Column(db.Integer)
    request = db.relationship("Child", backref=backref("users", uselist=False))

class Wants(db.Model):
    __tablename__ = 'wants'
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    wants_id = db.Column(db.Integer, primary_key=True)
    vacation = db.Column(db.Integer)
    clothing = db.Column(db.Integer)
    other = db.Column(db.Integer)
    request = db.relationship("Child", backref=backref("users", uselist=False))