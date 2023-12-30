
# Create a function called main()
# This function will control the flow of the whole program
def main():
  # Uses a while True loops to 
  while True:
    # Call userMenu() to display menu choices
    userMenu()
    # Call the function userInput
    # Assign function with variables inputNum1,inputNum2,choiceMenu
    inputNum1,inputNum2,choiceMenu = userInput()
    # Use an if/elif/else statement to call the requested functions
    if choiceMenu == 'x':
      # display message if none of the choices are selected 
      print('Program Exiting')
      break
    elif choiceMenu == 1:
      # Calls the function, passes the variable intputNum1 and inputNum2
      answer = add(inputNum1,inputNum2)
      # Assign requested operator to variable op
      op = '+'
    elif choiceMenu == 2:
      # Calls the function, passes the variable intputNum1 and inputNum2
      answer = subtract(inputNum1,inputNum2)
      # Assign requested operator to variable op
      op = '-'
    elif choiceMenu == 3:
       # Calls the function, passes the variable intputNum1 and inputNum2
      answer = multiply(inputNum1,inputNum2)
      # Assign requested operator to variable op
      op = '*'
    elif choiceMenu == 4:
       # Calls the function, passes the variable intputNum1 and inputNum2
      answer = divide(inputNum1,inputNum2)
      # Assign requested operator to variable op
      op = '/'
    elif choiceMenu == 5:
       # Calls the function, passes the variable intputNum1 and inputNum2
      answer = modulo(inputNum1,inputNum2)
      # Assign requested operator to variable op
      op = '%'
    elif choiceMenu == 6:
       # Calls the function, passes the variable intputNum1 and inputNum2
      answer = exponent(inputNum1,inputNum2)
      # Assign requested operator to variable op
      op = '**'
      # If none of the statements work then do this instead
    else: 
      pass 
    # Calls the function, passes the 4 variables to function userOutput()
    userOutput(inputNum1,inputNum2,answer,op)
# Create a function called userMenu()
# This function with  display all of the choice available to the user 
def userMenu():
  print()
  print('Select the action you\'d like to take, by number:')
  print('  1. Add')
  print('  2. Subtract')
  print('  3. Multiply')
  print('  4. Divide')
  print('  5. Modulo')
  print('  6. Exponent')
  print('  Any other number to exit the program')
  
# Create a function called userInput()
# This function will ask the user to select a menu option and to enter two numbers 
def userInput():
  
  choice = inputTest(input('Enter the menu item you would like to run: '))
  #Use an if/else statement to determine if number is in range of menu
  if choice in range(1,7):
    number1 = inputTest(input('Enter your first number: '))
    number2 = inputTest(input('Enter your second number: '))
  else:
    choice = "x" 
    number1 = 'x'
    number2 = 'x'
  
  #return all three numbers to main()
  return number1,number2,choice

# Create a function called inputTest()
# This function will test the input from function userInput() to determine is the input are string or an int,float
def inputTest(myNum):
  while True:
    # Use a try/except statement to test the numbers
    try:

      return float(myNum)
      break
      # If one or all of the numbers is a string in a int or a float display an error message
    except:
      myNum = input('Not a valid number. Enter your number you ')
  
# Create a function called add()
# This function will accept the two numbers and return the sum 
def add(n1,n2):
  Sum = n1 + n2

  an1 = float(Sum)

  return an1
# Create a function called subtract()
# This function will accept the two numbers and return the difference between them
def subtract(n1,n2):
  
  differ = n1 - n2

  an2 = float(differ)

  return an2
# Create a function called multiply()
# This function will accept the two numbers and return the product
def multiply(n1,n2):
  
  mult = n1 * n2

  an3 = float(mult)

  return an3
# Create a function called divide()
# This fucnction will accept the two numbers and return the quotient 
def divide(n1,n2):
  # Use try to watch code for errors 
  try:
    
    quotient = n1/n2

    an4 = float(quotient)

    return an4
    # Expection to run if code blocks throws an error
  except:
    return('Divide by 0 Not Allowed')
# Create a function called modulo()
# This fucnction will accept the two numbers and returns the mondulo
def modulo(n1,n2):
  # Use try to watch code for errors 
  try:
    # Take the two integers and divide them, use % to calculate the remainder 
    Mon = n1 % n2
    # Convert the integer to float
    # Assign the float to variable An5 
    an5 = float(Mon)
    # return the mondulo
    return an5
    # Expection to run if code blocks throws an error
  except:
    # Error shown to user 
    return ( 'Divide by 0 Not Allowed')
def exponent(n1,n2):
  # Take the first integer and raise it to the power of the second integer
  # Assign the integer to variable Exo
  Exo = n1 ** n2
  # Convert integer to float 
  # Assign float to variable An6
  an6 = float(Exo)
  # Return the exponent 
  return an6
# Create a function called userOutput() 
# This function will print all of the calculations 
def userOutput(n1,n2,an,op):
  #Use an if/else statement to display the selected calculations 
  if (an == 0):
    print('error')
  else: 
    print(n1,op,n2,'=',an)

if __name__ == '__main__':
    main()