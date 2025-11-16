def addition(a, b):
    return a + b   
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
       raise ZeroDivisionError("Can't be divided by zero")
    return a/b

# Main Program
def main():
    symbol = {
        '+': addition,
        '-': minus,
        '*': multiply,
        ':': divide
    }
    calculation_symbol = input('Please enter the calculation_symbol: +, -, *, : \n')
    if calculation_symbol in symbol:
        first_num = int(float(input('Please enter the first number:\n')))
        second_num = int(float(input('Please enter the second number:\n')))
        result = symbol[calculation_symbol](first_num, second_num)
        print('The result of', first_num, calculation_symbol, second_num, 'is', result)
    else:
        print('Invalid calculation symbol!') 
main()
#Author: Long Vien