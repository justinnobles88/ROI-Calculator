class ROICalculator():
    def monthlyIncome(self):
            print("Please input all values as numbers!")
            while True:
                rIncome = input("What is the total rental income your receive? ")
                if rIncome.isdigit():
                    print("Great!")
                    break
                else: 
                    print("Please enter numbers! ")
                    continue
            while True:
                miscIncome = input("What is the total for any other misc. income you receive? ")
                if miscIncome.isdigit():
                    print("Great!")
                    break
                else:
                    print("Please enter numbers!")
                    continue
            mIncome = int(rIncome) + int(miscIncome)
            print(f"Your total monthly income is: ${mIncome}.")

    def expenses(self):
        print("Please input all values as numbers!")
        expenses_dict = {}
        while True:
            ask_tax = input("What amount of taxes do you pay monthly? ")
            if ask_tax.isdigit():
                print("Great!")
                expenses_dict['Taxes'] = int(ask_tax)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            ask_insurance = input("What amount of insurance do you pay monthly?")
            if ask_insurance.isdigit():
                print("Great!")
                expenses_dict['Insurance'] = int(ask_insurance)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            utilities = input("Do you pay for any utilities?\nPlease enter 'Yes' or 'No': ")
            if utilities.lower() == 'yes':
                while True:
                    ask_water = input("What amount for Water/Sewer do you pay? ")
                    if ask_water.isdigit():
                        print("Great!")
                        expenses_dict["Water/Sewer"] = int(ask_water)
                        break
                    else:
                        print("Please enter a number!")
                        continue
                while True:
                    ask_garbage = input("What amount for garbage do you pay? ")
                    if ask_garbage.isdigit():
                        print("Great!")
                        expenses_dict["Garbage"] = int(ask_garbage)
                        break
                    else:
                        print("Please enter a number!")
                        continue
                while True:
                    ask_electric = input("What amount for electric do you pay? ")
                    if ask_electric.isdigit():
                        print("Great!")
                        expenses_dict["Electric"] = int(ask_electric)
                        break
                    else:
                        print("Please enter a number!")
                        continue
                while True:
                    ask_gas = input("What amount for gas do you pay? ")
                    if ask_gas.isdigit():
                        print("Great!")
                        expenses_dict["Gas"] = int(ask_gas)
                        break
                    else:
                        print("Please enter a number!")
                        continue
            elif utilities == 'no':
                break
            else:
                print("Opps! Please try again!")
                continue
            break
        while True:
            ask_hoa = input("Do you have any HOA fees?\nPlease type 'yes' or 'no': ")
            if ask_hoa.lower() == 'yes':
                while True:
                    hoa_amount = input("What amount of fees do you pay monthly? ")
                    if hoa_amount.isdigit():
                        print("Great!")
                        expenses_dict["HOA"] = int(hoa_amount)
                        break
                    else:
                        print("Please enter a number!")
                        continue
            elif ask_hoa.lower() == 'no':
                break
            else:
                print("Opps! Please try again!")
                continue
            break
        while True:
            ask_lawn = input("What amount do you pay monthly for year round lawn maintenence? ")
            if ask_lawn.isdigit():
                print("Great!")
                expenses_dict["Lawn/Snow"] = int(ask_lawn)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            ask_vacant = input("What amount do you take out monthly for vacancies? ")
            if ask_vacant.isdigit():
                print("Great!")
                expenses_dict["Vacancy"] = int(ask_vacant)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            ask_repair = input("What amount do you take out monthly for possible repairs? ")
            if ask_repair.isdigit():
                print("Great!")
                expenses_dict["Repairs"] = int(ask_repair)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            ask_capex = input("What amount do you take out monthly for Capital Expenses? ")
            if ask_capex.isdigit():
                print("Great!")
                expenses_dict["CapEx"] = int(ask_capex)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            ask_manage = input("What amount do you put toward property management each month? ")
            if ask_manage.isdigit():
                print("Great!")
                expenses_dict["Property Management"] = int(ask_manage)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            ask_mortgage = input("What amount is your monthly mortgage? ")
            if ask_mortgage.isdigit():
                print("Great!")
                expenses_dict["Mortgage"] = int(ask_mortgage)
                break
            else:
                print("Please enter a number!")
                continue
        values = expenses_dict.values()
        monthly_expenses = sum(values)
        print(f"Here are all of your expenses!\n")
        for k,v in expenses_dict.items():
            print(f"{k}: ${v}")
        print(f"\nYour total monthly expenses are: ${monthly_expenses}\n")

    def cashFlow(self):
        print("Please enter all values as numbers!\n")
        while True:
            monthly_income = input("What is your total monthly income? ")
            if monthly_income.isdigit():
                print("Great!")
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            expenses = input("What are your total expenses? ")
            if expenses.isdigit():
                print("Great!")
                break
            else:
                print("Please enter a number!")
                continue
        total_m_cashflow = int(monthly_income) - int(expenses)
        print(f"\nYour total monthly cash flow is: ${total_m_cashflow}\n")
        total_y_cashflow = total_m_cashflow * 12
        print(f"And your yearly cashflow is: ${total_y_cashflow}\n")

    def returnOnInvest(self):
        print("Please enter all valeus as numbers!\n")
        investment_dict = {}
        while True:
            down_pay = input("What was your down payment on the property? ")
            if down_pay.isdigit():
                print("Great!")
                investment_dict["Down Payment"] = int(down_pay)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            closing_cost = input("What were the closing costs? ")
            if closing_cost.isdigit():
                print("Great!")
                investment_dict["Closing Costs"] = int(closing_cost)
                break 
            else:
                print("Please enter a number!")
                continue
        while True:
            rehab = input("What was your rehab budget? ")
            if rehab.isdigit():
                print("Great!")
                investment_dict["Rehab Budget"] = int(rehab)
                break
            else:
                print("Please enter a number!")
                continue
        while True:
            misc = input("What were any other misc. costs for the property? ")
            if misc.isdigit():
                print("Great!")
                investment_dict["Other Misc."] = int(misc)
                break
            else:
                print("Please enter a number!")
                continue
        invest_values = investment_dict.values()
        total_investment = sum(invest_values)
        print(f"\nYour total investment for this property is: ${total_investment}\n")
        while True:
            cashflow = input("What is your monthly cash flow? ")
            if cashflow.isdigit():
                print("Great!")
                break
            else:
                print("Please enter a number!")
                continue
        returnOnInvest = ((int(cashflow)*12) / total_investment) * 100
        print(f"Your Cash on Cash ROI is: {round(returnOnInvest)}%\n")

def run():
    ROICalculator()
    while True:
        ask = input("What would you like to calculate:\nIncome/expenses/cashflow/ROI/quit? ")
        if ask.lower() == 'income':
            ROICalculator().monthlyIncome()
        elif ask.lower() == 'expenses':
            ROICalculator().expenses()
        elif ask.lower() == 'cashflow':
            ROICalculator().cashFlow()
        elif ask.lower() == "roi":
            ROICalculator().returnOnInvest()
        elif ask.lower() == 'quit':
            break
        else:
            print("\nThat is not okay!\n")
            continue

run()