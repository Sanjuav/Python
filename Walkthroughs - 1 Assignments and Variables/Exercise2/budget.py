print("My budget")
# All figures monthly
income=1000
# £3 coffee, 5 days per week, 4 weeks per month
coffee = 3 * 5 * 4
# £50 gas, 4 weeks per month
diesel = 50 * 4
print(f"My available income per month is £ {income}")
expenditure = coffee + diesel
print(f"My expenditure per month is £ {expenditure}")
budget=income-(coffee+diesel)
print(f"This leaves me with £ {budget} to spend each month")