import csv
file_path = 'sampleData.csv'

# Function reads attached csv file
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)
        print(headers)
        for row in csv_reader:
            data.append(row)
    return data

# 1. Function prints results of the currencies used
def currencies(file_path):
    currencies_used = set()

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            currency = row['Valiuta']
            currencies_used.add(currency)

        # income = float(row['Suma'])
        # if row['D/K'] == 'K':
        #     total_income += income
        #
        # outcome = float(row['Suma'])
        # if row['D/K'] == 'D':
        #     total_outcome += outcome
        #
        #     amount = float(row['Suma'])
        #     if row['D/K'] == 'K':
        #         total_income += amount
        #     elif row['D/K'] == 'D':
        #         total_outcome += amount
    return currencies_used

# 1. Function prints results of the currencies used
def print_currency(currencies_used):
    print("These currencies were used:", currencies_used)

def process_csv(file_path):
    currencies_used = set()
    total_income = 0
    total_outcome = 0

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            currency = row['Valiuta']
            currencies_used.add(currency)

        # income = float(row['Suma'])
        # if row['D/K'] == 'K':
        #     total_income += income
        #
        # outcome = float(row['Suma'])
        # if row['D/K'] == 'D':
        #     total_outcome += outcome

            amount = float(row['Suma'])
            if row['D/K'] == 'K':
                total_income += amount
            elif row['D/K'] == 'D':
                total_outcome += amount
    return total_income, total_outcome

# 2. Function prints results of total income and total outcome
def print_results(total_income, total_outcome):
    print("Total income (currencies are ignored):", total_income)
    print("Total outcome (currencies are ignored):", total_outcome)

# 3. Function calculates total income and total outcome by currency
def cal_income_outcome_by_currency(file_path):
    income_by_currency = {}
    outcome_by_currency = {}

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            currency = row['Valiuta']
            amount = float(row['Suma'])

            if row['D/K'] == 'K':
                if currency in income_by_currency:
                    income_by_currency[currency] += amount
                elif income_by_currency == 0:
                    print("income_by_currency[currency] = 'No income'")
                else:
                    income_by_currency[currency] = amount
            elif row['D/K'] == 'D':
                if currency in outcome_by_currency:
                    outcome_by_currency[currency] += amount
                else:
                    outcome_by_currency[currency] = amount
    return income_by_currency, outcome_by_currency

# 3. Function prints result of total income and total outcome by currency
def print_income_outcome_by_currency(income_by_currency, outcome_by_currency):
    print("Total income by currency:", )
    for currency, total_income in income_by_currency.items():
        print(f"{currency}: {total_income}")

    print("\nTotal outcome by currency:")
    for currency, total_outcome in outcome_by_currency.items():
        print(f"{currency}: {total_outcome}")

# 4. Function calculates total expenses by month
def cal_expenses_by_month(file_path):
    outcome_by_month = {}
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            date = row['Data']
            amount = float(row['Suma'])
            month = date.split('-')[1]

            if row['D/K'] == 'D':
                if month in outcome_by_month:
                    outcome_by_month[month] += amount
                else:
                    outcome_by_month[month] = amount
    return outcome_by_month

# 4. Function prints result of total expenses by month
def print_expenses_by_month(outcome_by_month):
    print(f"Total expenses by month:")
    for month, total_outcome in outcome_by_month.items():
        print(f"{month}: {total_outcome}")

# 5. Function calculates total income by month
def cal_income_by_month(file_path):
    income_by_month = {}
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            date = row['Data']
            amount = float(row['Suma'])
            month = date.split('-')[1]

            if row['D/K'] == 'K':
                if month in income_by_month:
                    income_by_month[month] += amount
                else:
                    income_by_month[month] = amount
    return income_by_month

# 5. Function prints result of total income by month
def print_income_by_month(income_by_month):
    print(f"Total income by month:")
    for month, total_income in income_by_month.items():
        print(f"{month}: {total_income}")

# 6. Function calculates total account balance in the end of each month
def cal_balance_by_month(file_path):
    income_in_end_month = {}
    outcome_in_end_month = {}
    balance_in_end_month = {}
    balance = 0.00

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            date = row['Data']
            amount = float(row['Suma'])
            month = date.split('-')[1]
            if row['D/K'] == 'K':
                if month in income_in_end_month:
                    income_in_end_month[month] += amount
                else:
                    income_in_end_month[month] = amount
            elif row['D/K'] == 'D':
                if month in outcome_in_end_month:
                    outcome_in_end_month[month] += amount
                else:
                    outcome_in_end_month[month] = amount

    for month in sorted(set(list(income_in_end_month.keys()) + list(outcome_in_end_month.keys()))):
        total_income = income_in_end_month.get(month, 0)
        total_outcome = outcome_in_end_month.get(month, 0)
        balance += total_income - total_outcome
        balance_in_end_month[month] = balance

    return balance_in_end_month

# 6. Function prints result of account balance in the end of each month
def print_balance_by_month(balance_by_month):
    print(f"Balance in the end of each month (currencies are ignored):")
    for month, balance in balance_by_month.items():
        print(f"Month {month}: {balance}")

# 7. Function calculates account balance by currency in the end of each month
def calc_monthly_balance_by_currency(file_path):
    bal_by_month_and_currency = {}

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            date = row['Data']
            amount = float(row['Suma'])
            month = date.split('-')[1]
            currency = row['Valiuta']

            if month not in bal_by_month_and_currency:
                bal_by_month_and_currency[month] = {}
            if currency not in bal_by_month_and_currency[month]:
                bal_by_month_and_currency[month][currency] = 0.0
            if row['D/K'] == 'K':
                bal_by_month_and_currency[month][currency] += amount
            elif row['D/K'] == 'D':
                bal_by_month_and_currency[month][currency] -= amount

    return bal_by_month_and_currency

# 7. Function prints result of account balance in the end of each month
def print_monthly_balance(bal_by_month_and_currency):
    print("Balance in the end of each month by currency:")
    for month, balances in bal_by_month_and_currency.items():
        print(f"Month {month}:")
        for currency, balance in balances.items():
            print(f"Currency {currency}: {balance:.2f}")

# 8. Function calculates income and outcome by month and currency

def calc_income_outcome_month_currency(file_path):
    income_by_month_currency = {}
    outcome_by_month_currency = {}

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            date = row['Data']
            month = date.split('-')[1]
            currency = row['Valiuta']
            amount = float(row['Suma'])

            if row['D/K'] == 'K':
                if (month, currency) in income_by_month_currency:
                    income_by_month_currency[(month, currency)] += amount
                else:
                    income_by_month_currency[(month, currency)] = amount
            elif row['D/K'] == 'D':
                if (month, currency) in outcome_by_month_currency:
                    outcome_by_month_currency[(month, currency)] += amount
                else:
                    outcome_by_month_currency[(month, currency)] = amount
    return income_by_month_currency, outcome_by_month_currency

# Function calculates the percentage expression of income and outcome by month and currency

def calc_percentage_income_outcome(file_path):
    income_by_month_currency, outcome_by_month_currency = calc_income_outcome_month_currency(file_path)
    total_income_by_month = {}
    total_outcome_by_month = {}
    percent_inc_out_month_curr = {}

    for month_currency, income in income_by_month_currency.items():
        month, currency = month_currency
        total_income_by_month[month] = total_income_by_month.get(month, 0) + income

    for month_currency, outcome in outcome_by_month_currency.items():
        month, currency = month_currency
        total_outcome_by_month[month] = total_outcome_by_month.get(month, 0) + outcome

    for month_currency, income in income_by_month_currency.items():
        month, currency = month_currency
        outcome = outcome_by_month_currency.get(month_currency, 0)

        total_income = total_income_by_month.get(month, 0)
        total_outcome = total_outcome_by_month.get(month, 0)

        income_percent = (income / total_income) * 100 if total_income > 0 else 0
        outcome_percent = (outcome / total_outcome) * 100 if total_outcome > 0 else 0

        # if total_income > 0:
        #     income_percent = (income / total_income) * 100
        # else:
        #     0
        # if total_outcome > 0:
        #     outcome_percent = (outcome / total_outcome) * 100
        # else:
        #     0
        if month not in percent_inc_out_month_curr:
            percent_inc_out_month_curr[month] = {}

        percent_inc_out_month_curr[month][currency] = {'Income': income_percent, 'Outcome': outcome_percent}

    return percent_inc_out_month_curr

# Function prints the result of percentage expression of income and outcome by month and currency
def print_percentage_income_outcome(percent_inc_out_month_curr):
    print("Percentage value of income and outcome by month and currency:")
    for month, currencies in percent_inc_out_month_curr.items():
        print(f"Month {month}:")
        for currency, percentages in currencies.items():
            print(f"Currency {currency}: Income: {percentages['Income']:.2f}%, Outcome: {percentages['Outcome']:.2f}%")

# def calc_percentage_income_outcome(file_path):
#     income_by_month = cal_income_by_month(file_path)
#     expenses_by_month = cal_expenses_by_month(file_path)
#     total_income = sum(income_by_month.values())
#     total_expenses = sum(expenses_by_month.values())
#
#     percent_inc_out_month = {}
#
#     for month, income in income_by_month.items():
#         expense = expenses_by_month.get(month, 0)
#         if total_income > 0:
#             income_percent = (income / total_income) * 100
#         else:
#             income_percent = 0
#         if total_expenses > 0:
#             expense_percent = (expense / total_expenses)
#         else:
#             expense_percent = 0
#         percent_inc_out_month[month] = {'Income': income_percent, 'Expenses': expense_percent}
#     return percent_inc_out_month

# Function prints the result of percentage expression of income and outcome by month
# def print_percentage_income_outcome(percent_inc_out_month):
#     print("Percentage value of income and outcome by month and currency:")
#     for month, percentages in percent_inc_out_month.items():
#         print(f"Month {month}: Income: {percentages['Income']:.2f}%, Expenses: {percentages['Expenses']:.2f}%")

