#-------------------------------------------------------------------------------
# Name:        Calculator
# Purpose:     Fun
#
# Author:      nicolescu
#
# Created:     21/12/2021
# Copyright:   (c) nicol 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
logo = '''
____________
| ________ |
||12345678||
|""""""""""|
|[M|#|C][-]|
|[7|8|9][+]|
|[4|5|6][x]|
|[1|2|3][%]|
|[.|O|:][=]|
"----------" '''

print(logo)
#Now we create the functions
def add (n1, n2):
    return n1 + n2

def substraction (n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def modulo (n1, n2):
    return n1 % n2

def power (n1, n2):
    return n1 ** n2

def calculator():
    num1 = float(input("What's the first number: \n"))
    operations = {"+": add, "-": substraction, "*": multiply, "/": divide, "%": modulo, "**": power}
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:

        operation_symbol = input("Pick operation: ")
        num2 = float(input("What's the next number: \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue or 'n' to exit: ") == 'y'.lower():
            num1 is answer
        else:
            should_continue = False
            calculator()

calculator()
