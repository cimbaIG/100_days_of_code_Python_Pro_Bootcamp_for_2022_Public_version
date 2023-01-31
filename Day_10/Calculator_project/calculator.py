import art
import os

# Lambda function to clear console screen
clear = lambda: os.system("clear")

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    num1 = float(input("What's the first number? "))
    num2 = float(input("What's the second number? "))

    for symbol in operations:
        print(symbol)

    continue_calculating = True
    while continue_calculating:
        operation_symbol = input("Pick an operation: ")

        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        yesNo = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()

        if yesNo == "y":
            num2 = int(input("What's the next number?: "))
            num1 = answer
        else:
            continue_calculating = False
            clear()
            calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculator()

# Their solution
""" from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator() """