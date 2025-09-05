#calculator
#add
def add(n1,n2):
    return n1 + n2
#subtract
def subtract(n1,n2):
    return n1-n2
#multifply
def multifply(n1,n2):
    return n1*n2
#divide
def divide(n1,n2):
    return n1/n2
#modulus
def modulus(n1,n2):
    return n1%n2
#floor division
def floor_division(n1,n2):
    return n1/n2
#exponentiation
def exponentiation(n1,n2):
    return n1**n2   

operations = {
    "+": add,
    "-": subtract,
    "*": multifply,
    "/": divide,
    "%": modulus,
    "//": floor_division,
    "**": exponentiation
}
num1 = int(input("Enter first number: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("Enter second number: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")
