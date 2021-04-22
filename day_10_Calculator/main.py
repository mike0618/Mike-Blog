from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def power(n1, n2):
    return n1 ** n2

operations = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
    '**': power,
}
def calculator():
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)

    proceed = 'y'
    while proceed == 'y':
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}\n")
        proceed = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'exit' to exit: ")
        if proceed == 'exit':
            return 'Bye'
        num1 = answer
    calculator()

calculator()
