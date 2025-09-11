# Write your divisible_by_ten() function here:
def divisible_by_ten(num): # function takes a number as input and evaluates if it is divisible evenly by 10. If so, it returns True. Otherwise, it returns False
  if num%10 == 0:
    return True
  else:
    return False


# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20)) # Function is called to test if 20 is evenly divisible by 10
# should print True
print(divisible_by_ten(25)) # Function is called to test if 25 is evenly divisible by 10
# should print False