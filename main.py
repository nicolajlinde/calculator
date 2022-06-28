import art


# add
def add(n1, n2):
    return n1 + n2


# Substract
def substract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)

    num1 = float(input("What's the first number?: "))

    for k in operations:
        print(k)

    end_calc = False
    while not end_calc:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        op = operations.get(operation_symbol)

        if op is not None:
            res = op(num1, num2)
        else:
            print("Did you type the right symbol?")

        print(f"{num1} {operation_symbol} {num2} = {res}")

        con_calc = input(f"Type 'y' to continue calculating with {res}, or type 'n to exit: '")

        if con_calc == "n":
            end_calc = True
            calculator()
        else:
            num1 = res


calculator()
