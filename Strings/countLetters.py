letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniqueLetters = []
  for letter in word:
    if letter in letters and letter not in uniqueLetters:
      uniqueLetters.append(letter)
  return len(uniqueLetters)
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4