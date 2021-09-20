# ROI calcualtor
# it has 4 classes
    # Income class
    # Expenses class
    # Cash Flow class
    # ROI class

class Income():
    def __init__(self):
        self.sumofincome = []

    def income(self):
        
        rent = int(input("Enter your monthly rent income: "))
        self.sumofincome.append(rent)
        
        allincome = sum(self.sumofincome)
        return int(allincome)

class Expenses():
    def __init__(self):
        self.sumofexpenses = []

    def expenses(self):
        while True:
            mortgage = int(input("Enter your monthly mortgage payment: " ))
            self.sumofexpenses.append(mortgage)
            vacancy = int(input("Enter your monthly vacancy amount... Usually its around 10% of your monthly rent income: "))
            self.sumofexpenses.append(vacancy)

            repairs = int(input("Enter how much you set aside each monthly for repairs: "))
            self.sumofexpenses.append(repairs)
            taxes = int(input("Enter your monthly tax bill amount: "))
            self.sumofexpenses.append(taxes)
            insurance = int(input("Enter your monthly insurance amount: "))
            self.sumofexpenses.append(insurance)
            propertymanagement = int(input("Enter your monthly property management amount: "))
            self.sumofexpenses.append(propertymanagement)
            cap_ex = int(input("Enter how much you set aside each month for big replacements... i.e carpet/roof/water heater/etc replacements: "))
            self.sumofexpenses.append(cap_ex)
            
            allexpenses = sum(self.sumofexpenses)
            print(allexpenses)
            return int(allexpenses)

class Cashflow():
    def __init__(self, totalincome, totalexpenses):
        self.totalincome = totalincome
        self.totalexpenses = totalexpenses

    def cashflow(self):
        totalincome = self.allincome
        monthlycashflow = int(self.allincome) - int(self.allexpenses)
        return int(monthlycashflow)


class Roi():
    def __init__(self):
        pass

    def cash_roi(self):
        downpayment = input("Enter the amount you paid for a down payment: ")
        closingcosts = input("Enter how much you paid for closing costs: ")
        remodeling = input("Enter how much you spent on rehab/remodeling your property: ")

        totalinvestment = downpayment + closingcosts + remodeling
        annualcashflow = self.monthlycashflow * 12

        cashoncashroi = annualcashflow/totalinvestment
        return int(cashoncashroi)

new_money = Income()
out_money = Expenses()
net_cash = Cashflow(totalincome, totalexpenses)


def run():
    # this will have our loop to for control flow.
    while True:
        new_money.income()
        out_money.expenses()
        net_cash.cashflow()
        
        
        break
run()