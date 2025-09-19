#Write your function here
def max_num(nums):
  maxVal = nums[0]
  for item in nums:
    if item > maxVal:
      maxVal = item
  return maxVal
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))