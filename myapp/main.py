from flask import Blueprint, render_template, request, redirect, jsonify, make_response, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

from .helpers import taxCalculator, budgetOptions, ny_tax_brackets, nyc_tax_brackets, federal_brackets
from werkzeug.security import check_password_hash, generate_password_hash
from .models import db, User, Stats, Necessities, Savings, Wants, Badges

        
@main.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")

@login_required
@main.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    if request.method == "GET":
        grab = Stats.query.filter_by(user_id=current_user.id).first()
        info = taxCalculator(grab.income, grab.status, grab.deductions)
        return render_template("dashboard.html", info=info, title="Dashboard")
    else:
        req = request.get_json()
        if req["location"] == "specifics":
            vars = req['vars']
            type = req['type']
            if type == "necessities":
                rent1 = vars['0']
                groceries1 = vars['1']
                other1 = vars['2']
                check = Necessities.query.filter_by(user_id=current_user.id)
                if check is None:
                    new_instance = Necessities(rent=rent1, groceries=groceries1, other=other1)
                    db.session.add(new_instance)
                    db.session.commit()
                else:
                    check.rent = rent1
                    check.groceries = groceries1
                    check.other = other1
                    db.session.commit()
                res = make_response(jsonify({
                    "type": "necessities",
                    "vars": vars,
                }), 200)
                return res

            elif type == "savings":
                emergency1 = vars['0']
                retirement1 = vars['1']
                debt1 = vars['2']
                check = Savings.query.filter_by(user_id=current_user.id)
                if check is None: 
                    new_instance = Savings(emergency=emergency1, retirement=retirement1, debt=debt1)
                    db.session.add(new_instance)
                    db.session.commit()
                else: 
                    check.emergency = emergency1
                    check.retirement = retirement1
                    check.debt = debt1
                    db.session.commit()
                res = make_response(jsonify({
                    "type": "savings",
                    "vars": vars,
                }), 200)
                return res
            else: 
                #nothing for now 
                vacation1 = vars['0']
                clothing = vars['1']
                other = vars['2']
                check = Wants.query.filter_by(user_id=current_user.id)
                if check is None:
                    new_instance = Wants(vacation=vacation1, clothing=clothing, other=other)
                    db.session.add(new_instance)
                    db.session.commit()
                else:
                    check.vacation = vacation1
                    check.clothing = clothing
                    check.other = other 
                    db.session.commit()

                res = make_response(jsonify({
                "type": "wants",
                "vars": vars,
                }), 200)
                return res
        

@main.route("/budget", methods=["POST"])
def budget():
    if request.method == "POST":
        req = request.get_json()
        badge_select = Badges.query.filter_by(user_id=current_user.id).first()
        badge_select.badge = True
        db.session.commit()
        info = Stats.query.filter_by(user_id=current_user.id).first()
        leftovers = taxCalculator(info.income, info.status, info.deductions).leftover
        instance = budgetOptions(leftovers)
        if req['type'] == 3:
            budgetPlan = instance.custom(req['savings'],req['necessities'], req["wants"], leftovers)

            res = make_response(jsonify({
                "budgetPlan": budgetPlan,
                }), 200)
            return res
        
        elif req['type'] == 2:
            budgetPlan = instance.seventyTwentyTen(leftovers)

            res = make_response(jsonify({
                "budgetPlan": budgetPlan,
            }), 200)
            return res
        else:
            budgetPlan = instance.fiftyTwentyThirty(leftovers)

            res = make_response(jsonify({
                "budgetPlan": budgetPlan,
            }), 200)
            return res

        
@main.route("/aboutUs")
def aboutUs():
    if request.method == "GET":
        return render_template("aboutus.html", title="About Us")
    
@main.route("/badges")
def badges():
    return render_template("badges.html", title="Badges")