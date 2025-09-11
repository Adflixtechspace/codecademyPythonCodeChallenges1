# Write your twice_as_large function here:
def twice_as_large(num1,num2): # function takes 2 inputs, doubles num 2, then compares both numbers. Returns True if num1 is greater than num2, otherwise, returns false
  num2*=2
  if num1 > num2:
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5)) # calls function, checking if 10 is more than twice as large as 5
# should print False
print(twice_as_large(11, 5)) # calls function, checking if 11 is more than twice as large as 5
# should print True