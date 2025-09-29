# Write your substring_between_letters function here:
def substring_between_letters(word,start,end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index != -1 and end_index != -1:
    return word[start_index+1:end_index]
  else:
    return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
print(substring_between_letters("squigglyline", "i", "y"))
# should print "ggl"