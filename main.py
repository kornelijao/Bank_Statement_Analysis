# ---------------- BANK STATEMENT DATA FILE --------------
print("----------- BANK STATEMENT DATA FILE --------------")
import csv
# import functions as func

print()

file_path = 'sampleData.csv'
def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)
        print(headers)
        for row in csv_reader:
            data.append(row)
    return data

#  1) kokios valiutos buvo naudotos?
#  2) kiek income, outcome?(ignoruojant valiutas)
print()
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
    return currencies_used, total_income, total_outcome

def print_results(currencies_used, total_income, total_outcome):
    print("Part 1")
    print()
    print("These currencies were used:", currencies_used)
    print()
    print("Part 2")
    print("Total income (currencies are ignored):", total_income)
    print("Total outcome (currencies are ignored):", total_outcome)

file_path = 'sampleData.csv'
currencies_used, total_income, total_outcome = process_csv(file_path)
print_results(currencies_used, total_income, total_outcome)

#  3) Kiek income, outcome pagal kiekvieną valiutą?

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

def print_income_outcome_by_currency(income_by_currency, outcome_by_currency):
    print()
    print("Part 3")
    print("Total income by currency:", )
    for currency, total_income in income_by_currency.items():
        print(f"{currency}: {total_income}")

    print("\nTotal outcome by currency:")
    for currency, total_outcome in outcome_by_currency.items():
        print(f"{currency}: {total_outcome}")

file_path = 'sampleData.csv'
income, outcome = cal_income_outcome_by_currency(file_path)
print_income_outcome_by_currency(income, outcome)

# 4) kiek buvo išleista kiekvieną mėnesį?
print()
print("Part 4")

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

def print_expenses_by_month(outcome_by_month):
    print("Part 4")
    print(f"Expenses by month: {outcome_by_month}")
    for month, total_outcome in outcome_by_month.items():
        print(f"{month}: {total_outcome}")

file_path = 'sampleData.csv'
expenses = cal_expenses_by_month(file_path)
print_expenses_by_month(expenses)

# 5) kiek buvo uždirbta kiekvieną mėnesį?
print()
print("Part 5")

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

def print_income_by_month(income_by_month):
    print("Part 5")
    print(f"Income by month: {income_by_month}")
    for month, total_income in income_by_month.items():
        print(f"{month}: {total_income}")

file_path = 'sampleData.csv'
income = cal_income_by_month(file_path)
print_income_by_month(income)

# 6) koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas).
print()
print("Part 6")

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

def print_balance_by_month(balance_by_month):
    print(f"Balance in the end of each month: {balance_by_month}")
    for month, balance in balance_by_month.items():
        print(f"Month {month}: {balance}")

file_path = 'sampleData.csv'
balances = cal_balance_by_month(file_path)
print_balance_by_month(balances)

# 7) Koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?
print()
print("Part 7")

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

def print_monthly_balance(bal_by_month_and_currency):
# result = calc_monthly_balance_by_currency(file_path)
    for month, balances in bal_by_month_and_currency.items():
        print(f"Month {month}:")
        for currency, balance in balances.items():
            print(f"Currency {currency}: {balance}")

file_path = 'sampleData.csv'
result = calc_monthly_balance_by_currency(file_path)
print_monthly_balance(result)

# 7) Atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška.

def print_percentage_income_outcome_by_month(file_path):
    income_by_month = cal_income_by_month(file_path)
    expenses_by_month = cal_expenses_by_month(file_path)
    total_income = sum(income_by_month.values())
    total_expenses = sum(expenses_by_month.values())

    percent_inc_out_month = {}

    for month, income in income_by_month.items():
        expense = expenses_by_month.get(month, 0)
        if total_income > 0:
            income_percent = (income / total_income) * 100
        else:
            income_percent = 0
        if total_expenses > 0:
            expenense_percent = (expense / total_expenses)
        else:
            outcome_percent = 0

        percent_inc_out_month[month] = {'Income': income_percent, 'Expenses': expenense_percent}

    print("Percentage value of income and outcome by month:")
    for month, percentages in percent_inc_out_month.items():
        print(f"Month {month}: Income: {percentages['Income']:.2f}%, Expenses: {percentages['Expenses']:.2f}%")

file_path = 'sampleData.csv'
print_percentage_income_outcome_by_month(file_path)



