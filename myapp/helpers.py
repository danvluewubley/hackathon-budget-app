import os, sys


#New York State tax bracket dictionary
ny_tax_brackets = [
    {"rate": 4.00, "s": (0, 8500), "mfj": (0, 17150), "hoh": (0, 12800)},
    {"rate": 4.50, "s": (8501, 11700), "mfj": (17151, 23600), "hoh": (12801, 17650)},
    {"rate": 5.25, "s": (11701, 13900), "mfj": (23601, 27900), "hoh": (17651, 20900)},
    {"rate": 5.90, "s": (13901, 21400), "mfj": (27901, 43000), "hoh": (20901, 32200)},
    {"rate": 6.33, "s": (21401, 80650), "mfj": (43001, 161550), "hoh": (32201, 107650)},
    {"rate": 6.57, "s": (80651, 215400), "mfj": (161551, 323200), "hoh": (107651, 269300)},
    {"rate": 6.85, "s": (215401, 1077550), "mfj": (323201, 2155350), "hoh": (269301, 1616450)},
    {"rate": 9.65, "s": (1077551, 5000000), "mfj": (2155351, 5000000), "hoh": (1616451, 5000000)},
    {"rate": 10.30, "s": (5000001, 25000000), "mfj": (5000001, 25000000), "hoh": (5000001, 25000000)},
    {"rate": 10.90, "s": (25000001, float('inf')), "mfj": (25000001, float('inf')), "hoh": (25000001, float('inf'))}
]

       
#Federal tax brackets dictionary
federal_brackets = [
    {"rate": 10, "s": (0, 11000), "mfj": (0, 22000), "hoh": (0, 15700)},
    {"rate": 12, "s": (11001, 44725), "mfj": (22001, 89450), "hoh": (15701, 59850)},
    {"rate": 22, "s": (44726, 95375), "mfj": (89451, 190750), "hoh": (59851, 95350)},
    {"rate": 24, "s": (95376, 182100), "mfj": (190751, 364200), "hoh": (95351, 182100)},
    {"rate": 32, "s": (182101, 231250), "mfj": (364201, 462500), "hoh": (182101, 231250)},
    {"rate": 35, "s": (231251, 578125), "mfj": (462501, 693750), "hoh": (231251, 578100)},
    {"rate": 37, "s": (578126, float('inf')), "mfj": (693751, float('inf')), "hoh": (578101, float('inf'))}]

#New York City Tax Brackets
nyc_tax_brackets = [
    {"rate": 3.078, "s": (0, 12000), "mfj": (0, 21600), "hoh": (0, 14400)},
    {"rate": 3.762, "s": (12001, 25000), "mfj": (21601, 45000), "hoh": (14401, 30000)},
    {"rate": 3.819, "s": (25001, 50000), "mfj": (45001, 90000), "hoh": (30001, 60000)},
    {"rate": 3.876, "s": (50001, float('inf')), "mfj": (90001, float('inf')), "hoh": (60001, float('inf'))}
]

class taxCalculator:
    
    def __init__(self, income, agiVal, status, deductions):
        self.status = status
        self.income = income
        self.taxes = 0
        #Checks if the value given is already adjusted gross income or not
        if agiVal == True:
            self.agi = self.income
        else:
            self.agi = self.fagi(income, status, deductions)
        self.social = self.social_sec(income)
        self.medi = self.medicare(income, status)

        self.agi = self.agi - self.medi
        self.agi = self.agi - self.social
        #Calculated the amount of taxes you must pay
        self.taxes += self.federal(self.agi,status)
        self.taxes += self.state(self.agi,status)
        self.taxes += self.city(self.agi,status)

        self.fed = self.federal(self.agi, status)
        self.cit = self.federal(self.agi, status)
        self.sta = self.state(self.agi, status)
        self.leftover = (self.income - self.taxes)/12


    
    #Calculates Federal Adjusted Gross Income
    def fagi(self, income, status, deductions):
        agi = income
        #Checks for status of the tax filer and then removes their standard deduction from their agi
        if status == 's': 
            agi = agi - 13850
        elif status == 'mfj':
            agi = agi - 27700
        elif status == "hoh":
            agi = agi - 20800
        else:
            agi = agi - 27700

        #Subtracts any additional deductions the tax filer might have from their agi 
        agi = agi - deductions


        return agi

    # Calculates state taxes
    def state(self, agi, status):
        taxable_income = 0
        #Iterates through all tax brackets until it reaches highest tax bracket for income and then ends loop.
        for i in len(ny_tax_brackets):
            #If agi is greater than the upper threshold of bracket subtract lower threshold from upper threshold and then multiply difference by bracket rate
            if agi > ny_tax_brackets[i][status][1] :
                taxable_income += (ny_tax_brackets[i][status][1] - ny_tax_brackets[i][status][0]) * ny_tax_brackets[i]["rate"]
            #If agi is smaller subtract lower threshold from agi and then multiply the difference by the bracket rate. Then the loop breaks
            elif agi <= ny_tax_brackets[i][status][1]:
                taxable_income += (agi - ny_tax_brackets[i][status][0]) * ny_tax_brackets[i]["rate"]
                break
        

        return taxable_income 
        
    #Calculates federal taxes
    def federal(self, agi, status ):
        taxable_income = 0
        #Refer to state tax comments
        #Same process as state tax calculation but with federal tax bracket
        for i in len(federal_brackets):
            
            if agi > federal_brackets[i][status][1] :
                taxable_income += (federal_brackets[i][status][1] - federal_brackets[i][status][0]) * federal_brackets[i]["rate"]
            elif agi <= federal_brackets[i][status][1]:
                taxable_income += (agi - federal_brackets[i][status][0]) * federal_brackets[i]["rate"]
                break
        

        return taxable_income 
    def city(self, agi, status):
        taxable_income = 0
        #Refer to state tax comments
        #Same process as state tax calculation but with federal tax bracket
        for i in len(nyc_tax_brackets):
            if agi > nyc_tax_brackets[i][status][1] :
                
                taxable_income += (nyc_tax_brackets[i][status][1] - nyc_tax_brackets[i][status][0]) * nyc_tax_brackets[i]["rate"]
            elif agi <= nyc_tax_brackets[i][status][1]:
                taxable_income += (agi - nyc_tax_brackets[i][status][0]) * nyc_tax_brackets[i]["rate"]
                break
        

        return taxable_income 
    
    
    def social_sec(self, income):
        taxable_income = 0 
        if income <= 168800:
            taxable_income = 0.062 * income
        else:
            taxable_income = 0.062 * 168800

        return taxable_income
    

    def medicare(self, income, status):
        taxable_income = 0
        if status == "mfj":
            if income < 250000:
                taxable_income = 0.0145 * income
            else:
                taxable_income= (0.0145 + 0.009) * income
        else:
            if income < 200000:
                taxable_income =  0.0145 * income
            else: 
                taxable_income = (0.0145 + 0.009)* income

        return taxable_income
        

class budgetOptions:

    def __init__(self, leftovers):
        self.totalBudget = leftovers


    def fiftyTwentyThirty(self, budget):
        dict = {}
        dict["needs"] = budget * 0.50
        dict["needs"] = budget * 0.30 
        dict["needs"] = budget * 0.20
        return dict
    

    def custom(self, budget, goals):
        return