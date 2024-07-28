from flask import Flask, flash, redirect, render_template, request, session, jsonify, make_response
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from helpers import taxCalculator, budgetOptions
app = Flask(__name__)


        
@app.route("/")
def index():

    return render_template("index.html")

@app.route("/login")
def login():
    return