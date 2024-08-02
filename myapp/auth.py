from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Stats
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login_post():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.password, password): 
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user, remember=remember)
        return redirect("/dashboard")
    else: 
        return render_template("login.html")
    

@auth.route("/sign-up")
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
    

@login_required
@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/index")
