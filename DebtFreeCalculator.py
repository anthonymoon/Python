import argparse

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Calculate savings over a 3-month period')

# Add the arguments for income, expenses, savings, and debt repayment
parser.add_argument('--income', type=float, help='The monthly income', default=6000)
parser.add_argument('--expenses', type=float, help='The monthly expenses', default=3000)
parser.add_argument('--savings', type=float, help='The initial savings amount', default=0)
parser.add_argument('--debt-repayment', type=float, help='The monthly debt repayment amount', default=1000)

# Parse the arguments
args = parser.parse_args()

# Set the variables to the values specified by the user
income = args.income
expenses = args.expenses
savings = args.savings
debt_repayment = args.debt_repayment

# Define a list to hold the results of the calculations
results = []

# Loop over a range of 3 months
for month in range(1, 4):
    # Calculate the net income for the month by subtracting expenses and debt repayment from income
    net_income = income - expenses - debt_repayment

    # Add the net income to the savings
    savings += net_income

    # Print the results for the current month
    print("Month: {}".format(month))
    print("Income: {}".format(income))
    print("Expenses: {}".format(expenses))
    print("Debt Repayment: {}".format(debt_repayment))
    print("Savings: {}".format(savings))
    print()

    # Append the results for the current month to the results list
    results.append({"month": month, "income": income, "expenses": expenses,
                   "debt_repayment": debt_repayment, "savings": savings})

# Print the final results
print("Final results:")
print(results)