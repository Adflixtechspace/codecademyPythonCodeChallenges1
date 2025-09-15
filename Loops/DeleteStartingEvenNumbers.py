#Write your function here
def delete_starting_evens(myList):
  while len(myList) > 0 and myList[0]%2 == 0:
    myList = myList[1:]
  return myList
    

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))