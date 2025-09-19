#Write your function here
def larger_sum(lst1, lst2):
  sumL1 = 0
  sumL2 = 0
  for l1 in lst1:
    sumL1 += l1
  for l2 in lst2:
    sumL2 += l2
  if sumL2 > sumL1:
    return lst2
  else:
    return lst1
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))