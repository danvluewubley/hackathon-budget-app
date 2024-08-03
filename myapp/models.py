from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    stats = db.relationship('Stats', backref='users', lazy=True )
    savings = db.relationship('Savings', backref='users', lazy=True)
    necessities = db.relationship('Necessities', backref='users', lazy=True)
    wants = db.relationship('Wants', backref='users', lazy=True)

class Stats (db.Model):
    __tablename__ = 'stats'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    stats_id = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Integer)
    deductions = db.Column(db.Integer)
    status = db.Column(db.Integer)
    location = db.Column(db.String(100))

class Savings (db.Model):
    __tablename__ = 'savings'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    savings_id = db.Column(db.Integer, primary_key=True)
    emergency = db.Column(db.Integer)
    retirement = db.Column(db.Integer)
    debts = db.Column(db.Integer)

class Necessities (db.Model):
    __tablename__ = 'necessities'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    necessities_id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    groceries = db.Column(db.Integer)
    other = db.Column(db.Integer)

class Wants(db.Model):
    __tablename__ = 'wants'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    wants_id = db.Column(db.Integer, primary_key=True)
    vacation = db.Column(db.Integer)
    clothing = db.Column(db.Integer)
    other = db.Column(db.Integer)

class Badges(db.Model):
    __tablename__ = 'badges'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    badge=db.Column(db.Boolean)