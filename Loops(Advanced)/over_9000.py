#Write your function here
def over_nine_thousand(lst):
  lstSum = 0
  for item in lst:
    lstSum += item
    if lstSum > 9000:
      break
  return lstSum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))