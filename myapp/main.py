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
        if current_user.isauthenticated():
            user = current_user
            stat = Stats.query.get(user.id)
            income = stat.income
            deductions = stat.deductions
            status = stat.status
        else:
            income = request.form.get("income")
            deductions = request.form.get("deductions")
            status = request.form.get("status")
        
        instance = taxCalculator(income, agiVal, status, deductions)

        

        return render_template("dashboard.html")



@main.route("/aboutUs")
def aboutUs():
    if request.method == "GET":
        return render_template("aboutus.html")