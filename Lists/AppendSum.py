# Write your function here
def append_sum(myList):
  for i in range(3):
    myList.append(myList[-2]+myList[-1])
  return myList

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
print(append_sum([4, 28]))