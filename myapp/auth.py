from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from .models import User, Stats, Badges
from . import db

auth = Blueprint('auth', __name__)
        
@auth.route('/login', methods=["POST"])
def login_post():    
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    remember = True if data.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.', 'danger')
        return jsonify({"success": False}), 401

    # Successful login
    login_user(user, remember=remember)
    flash("Login successful!", 'success')
    return jsonify({"success": True}), 200  
    


@auth.route("/sign-up", methods=["GET", "POST"])
def signUp():
    if request.method == "GET":
        return render_template("signup.html", title="Sign Up")
    
    if request.method == "POST":
        email1 = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        location1 = request.form.get("ny-or-nyc")
        deduction1 = request.form.get("deduction")
        status1 = request.form.get("status")
        
        if password != confirmation:
            return "Passwords do not match", 400
        
        hash = generate_password_hash(password)
        
        new_account = User(email=email1, password=hash)
        
        try:
            db.session.add(new_account)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"An error occurred while creating the account: {e}", 500

        current = User.query.filter_by(email=email1).first()
        
        if not current:
            return "User not found after creation", 500
        
        income1 = request.form.get("income")

        new_info = Stats(user_id=current.id, income=income1, location=location1, deductions=deduction1, status=status1)
        new_badge = Badges(user_id=current_user.id, badge=False)
        db.session.add(new_badge)
        db.session.commit()
        try:
            db.session.add(new_info)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"An error occurred while creating user stats: {e}", 500
        
        login_user(current)

        return redirect(url_for("main.dashboard"))

@login_required
@auth.route("/logout")
def logout():
    logout_user()
    return redirect("/")
