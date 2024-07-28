from flask import Flask
from flask_session import session 
app = Flask(__name__)

stateList = [0,
        8500, 
        11700,
        13900,
        80650,
        1077550,
        5000000, 
        25000000
        ]



class taxCalculator:
    
    def __init__(self, income, agiVal, status, deductions):
        self.status = status
        self.income = income
        if agiVal == True:
            self.agi = self.income
        else:
            self.agi = self.fagi(income, status, deductions)

        return 
    
    def fagi(self, income, status, deductions):
        agi = income
        if status == 's': 
            agi = agi - 13850
        elif status == 'mfj':
            agi = agi - 27700
        elif status == "mfs":
            agi = agi - 13850
        elif status == "hoh":
            agi = agi - 20800
        else:
            agi = agi - 27700

        agi = agi - deductions


        return agi

    def state(self):

        return 
    
    def federal(self):

        return
    
    def city(self):
        
        return

        
@app.route("/")
def index():
    return 