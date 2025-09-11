def large_power(base,exponent): # function used to calculate a base to a power and return true if it is greater than 5000 and False if not
  num = base**exponent
  if num > 5000:
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13)) # calls function, passing 2 is base and 13 is exponent
# should print True
print(large_power(2, 12)) # calls function, passing 2 is base and 12 is exponent
# should print False