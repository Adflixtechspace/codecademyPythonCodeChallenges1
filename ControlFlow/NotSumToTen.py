num1 = int(input("Please inpuut the first number: ")) # asks user to assign num1 with an integer value
num2 = int(input("Please inpuut the second number: ")) # asks user to with an integer value

# Write your if statement here
if num1+num2 != 10: # checks if the sum of num1 and num2 do not add up to 10
  not_ten=True # sets not_ten to True
else: # Runs if statement above is not true
  not_ten=False # sets not_ten to False

# Uncomment the below lines to show the result
print("Is the sum of the numbers not equal to 10? " + str(not_ten)) # Displays answer to the console