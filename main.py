print("----------- BANK STATEMENT DATA FILE --------------")
# import csv
import functions as func

file_path = 'sampleData.csv'

#  1) kokios valiutos buvo naudotos?
print()
print("Part 1")
currencies_used = func.currencies(file_path)
func.print_currency(currencies_used)

# 2) kiek income, outcome?(ignoruojant valiutas)
print()
print("Part 2")
total_income, total_outcome = func.process_csv(file_path)
func.print_results(total_income, total_outcome)

# 3) Kiek income, outcome pagal kiekvieną valiutą?
print()
print("Part 3")
income, outcome = func.cal_income_outcome_by_currency(file_path)
func.print_income_outcome_by_currency(income, outcome)

# 4) kiek buvo išleista kiekvieną mėnesį?
print()
print("Part 4")
expenses = func.cal_expenses_by_month(file_path)
func.print_expenses_by_month(expenses)

# 5) kiek buvo uždirbta kiekvieną mėnesį?
print()
print("Part 5")
income = func.cal_income_by_month(file_path)
func.print_income_by_month(income)

# 6) koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas).
print()
print("Part 6")
balances = func.cal_balance_by_month(file_path)
func.print_balance_by_month(balances)

# 7) Koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?
print()
print("Part 7")
result = func.calc_monthly_balance_by_currency(file_path)
func.print_monthly_balance(result)

# 8) Atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška.
print()
print("Part 8")
percentages = func.calc_percentage_income_outcome(file_path)
func.print_percentage_income_outcome(percentages)


