from flask import Flask, flash, redirect, render_template, request, session, jsonify, make_response
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from helpers import taxCalculator, budgetOptions
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
app = Flask(__name__)




app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

app.jinja_env.autoescape = True

Session(app)

csrf = CSRFProtect(app)
        
@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/login")
def login():

    email = request.form.get("email")
    password = request.form.get("password")
    if not check_password_hash(password):
        return ValueError

    return

@app.route("/sign-up")
def signUp():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        location = request.form.get("location")
        if password != confirmation:
            return ValueError
        hash = generate_password_hash(password)
        

        return 


@app.route("/dashboard")
def dashboard():
    if request.method == "GET":
        return render_template("dashboard.html")



@app.route("/aboutUs")
def aboutUs():
    if request.method == "GET":
        return render_template("aboutus.html")