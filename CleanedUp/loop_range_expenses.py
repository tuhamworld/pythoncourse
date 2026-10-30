# For certain number of expenses
# total = 0
# expenses = []

# for i in range(7):
#     expenses.append(float(input('Enter your expense:')))

# total = sum(expenses)
# print("You spent $", total, sep='')


# For user-defined number of times
new_total = 0
new_expenses = []
num_expenses = int(input("Enter # of expenses "))

for i in range(num_expenses):
    new_expenses.append(float(input('Enter an expense:')))

new_total = sum(new_expenses)
print("You spent $", new_total, sep='')