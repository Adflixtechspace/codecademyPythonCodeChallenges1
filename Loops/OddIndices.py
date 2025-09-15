#Write your function here
def odd_indices(myList):
  newList = []
  for count in range(1, len(myList), 2):
    newList.append(myList[count])
  return newList

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))