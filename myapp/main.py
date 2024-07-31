from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

from .helpers import taxCalculator, budgetOptions
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User, Stats

        
@main.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")



@main.route("/sign-up")
def signUp():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        email1 = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        location1 = request.form.get("location")
        if password != confirmation:
            return ValueError
        hash = generate_password_hash(password)
        
        new_account = User(email=email1, password=hash, location=location1)
        db.session.add(new_account)

        income1 = request.form.get("income")

        new_info = Stats(income=income1,  )

        db.session.add(new_info)

        db.session.commit()

        return redirect("/dashboard")


@main.route("/dashboard")
def dashboard():
    if request.method == "GET":
        user = current_user
        return render_template("dashboard.html")



@main.route("/aboutUs")
def aboutUs():
    if request.method == "GET":
        return render_template("aboutus.html")