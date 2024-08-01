from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

from .helpers import taxCalculator, budgetOptions, ny_tax_brackets, nyc_tax_brackets, federal_brackets
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User, Stats

        
@main.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")



@main.route("/dashboard")
def dashboard():
    if request.method == "GET":
        user = None
        deductions = 0
        income = 0 
        agiVal = False
        status = None
        user = current_user
        """
        req = request.get_json()
        if consistency(checkVars):
            res = make_response(jsonify({
                    "code": "green"
            }), 200)
            return res
        else:
            res = make_response(jsonify({
                "code": "red"
            }), 200)
            return res"""



        return render_template("dashboard.html")



@main.route("/aboutUs")
def aboutUs():
    if request.method == "GET":
        return render_template("aboutus.html")
    
@main.route("/badges")
def badges():
    return render_template("badges.html")