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

num1 = float(input("Enter first number: "))
for symbol in operations:
    print(symbol)
operations_symbol = input("Pick an operation from list: ")
num2 = float(input("Enter next number: "))

calculation_function = operations[operations_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")
