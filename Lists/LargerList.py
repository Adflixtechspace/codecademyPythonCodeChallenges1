# Write your function here
def larger_list(myList1,myList2):
  if len(myList1) >= len(myList2):
    return(myList1[-1])
  else:
    return(myList2[-1])

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))