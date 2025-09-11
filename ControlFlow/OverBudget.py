# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculates the total amount of expenses
total = food_bill+electricity_bill+internet_bill+rent # sets total bill to the sum of all monthly expenses

# Check if the total is greater than the budget and store the result in over_budget
if total>budget: # checks if the value of total is greater than the value of budget
  over_budget=True # sets over_budget to True
else: # runs if above if statement is false
  over_budget=False # sets over_budget to False

# Uncomment the below lines to see the results

print("Total: " + str(total)) # displays total bill
print("Is it over budget? " + str(over_budget)) # states if the total is over budget