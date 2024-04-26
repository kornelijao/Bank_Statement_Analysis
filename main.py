# ---------------- BANK STATEMENT DATA FILE --------------
print("----------- BANK STATEMENT DATA FILE --------------")
import csv
# import functions as func

print()

file_path = 'sampleData.csv'
with open(file_path, 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    headers = next(csv_reader)
    print(headers)
    for row in csv_reader:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

#  1) kokios valiutos buvo naudotos?
#  2) kiek income, outcome?(ignoruojant valiutas)
print()

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

print("Part 1")
print()
print("These currencies were used:", currencies_used)
print()
print("Part 2")
print("Total income (currencies are ignored):", total_income)
print("Total outcome (currencies are ignored):", total_outcome)

#  3) Kiek income, outcome pagal kiekvieną valiutą?

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

print()
print("Part 3")
print("Total income by currency:", )
for currency, total_income in income_by_currency.items():
    print(f"{currency}: {total_income}")

print("\nTotal outcome by currency:")
for currency, total_outcome in outcome_by_currency.items():
    print(f"{currency}: {total_outcome}")

# 4) kiek buvo išleista kiekvieną mėnesį?
print()
print("Part 4")

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

print(f"Expenses by month: {outcome_by_month}")

# 5) kiek buvo uždirbta kiekvieną mėnesį?
print()
print("Part 5")

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

print(f"Income by month: {income_by_month}")

# 6) koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas).
print()
print("Part 6")

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

print("Balance in the end of each month:")
for month, balance in balance_in_end_month.items():
    print(f"Month {month}: {balance}")

# 7) Koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?
print()
print("Part 7")

def calc_monthly_balance_by_currency(file_path):
    balance_by_month_and_currency = {}

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            date = row['Data']
            amount = float(row['Suma'])
            month = date.split('-')[1]
            currency = row['Valiuta']

            if month not in balance_by_month_and_currency:
                balance_by_month_and_currency[month] = {}
            if currency not in balance_by_month_and_currency[month]:
                balance_by_month_and_currency[month][currency] = 0.0
            if row['D/K'] == 'K':
                balance_by_month_and_currency[month][currency] += amount
            elif row['D/K'] == 'D':
                balance_by_month_and_currency[month][currency] -= amount

    return balance_by_month_and_currency

result = calc_monthly_balance_by_currency(file_path)
for month, balances in result.items():
    print(f"Month {month}:")
    for currency, balance in balances.items():
        print(f"Currency {currency}: {balance}")

# 7) Atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška.

