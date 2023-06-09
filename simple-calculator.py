import re #import regex module

print("Welcome to the basic calculator. Please follow the prompts below")

# I'm adding my random update to test git pull/push on multiple team members
while True:
  
  value = input("Enter a calcualtion or quit to exit: ")
  
  # check if user wants to quit
  if value.lower() == 'quit':
  
    break
  
  # use regex to check if the input is a valid calculation
  # the regex pattern '^[0-9+\-*/().\s]*$' matches any combination of digits, basic arithmetic operators, parentheses, and whitespace
  # the '^' and '$' anchors ensure that the entire string must match this pattern
  if not re.match('^[0-9+\-*/()%.\s]*$', value):
    print("Invalid calculation. Only numbers and basic arithmetic operators are allowed. Please try again.")
    continue
  
  try:
      answer = eval(value)
      print("The answer is:", answer)
      
  except:
      print("Invalid Operation. please try again or type quit to exit")