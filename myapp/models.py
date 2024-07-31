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
    user_id = db.Column(db.Integer, ForeignKey('request.id'))
    stats_id = db.Column(db.Integer, primary_key=True)
    request = db.relationship("Child", backref=backref("request", uselist=False))