#Write your function here
def reversed_list(lst1, lst2):
  matches = 0
  for i in range(len(lst1)):
    if lst1[i] == lst2[-(i+1)]:
      matches += 1
  if matches == len(lst1):
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))