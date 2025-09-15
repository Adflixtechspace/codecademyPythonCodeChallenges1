#Write your function here
def add_greetings(names):
  helloNames = []
  for name in names:
    helloNames.append("Hello, "+name)
  return helloNames

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))