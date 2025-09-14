# Write your function here
def more_than_n(myList,item,n):
  ncount = 0
  for i in myList:
    if i == item:
      ncount += 1
  if ncount > n:
    return True
  else:
    return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))