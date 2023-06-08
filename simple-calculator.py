print("Welcome to the basic calculator. Please follow the prompts below")


#testing git
value1 = float(input("What is your first value? "))
value3 = input("Enter your operator:")
value2 = float(input("What is your second value? "))
answer = str()


if value3 == "+":
  answer = value1 + value2
  
elif value3 == "-":
  answer = value1 - value2
  
elif value3 == "*":
  answer = value1 * value2
  
elif value3 == "/":
  answer = value1 / value2
  
else:
  print ("Invalid Operator")

print("The answer is:", answer)