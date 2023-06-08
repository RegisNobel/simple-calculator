print("Welcome to the basic calculator. Please follow the prompts below")

while True:
  
  value = input("Enter a calcualtion or quit to exit")
  

  if value.lower() == 'quit':
  
    break
  
  if any(char.isalpha() for char in value):
    print("Invalid Operation. Letters are not allowed. ")
  
  try:
      answer = eval(value)
      print("The answer is:", answer)
      
  except:
      print("Invalid Operation. please try again or type quit to exit")