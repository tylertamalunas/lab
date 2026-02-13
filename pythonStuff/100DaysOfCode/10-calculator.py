def calc(x, y, operation):
    if operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    elif operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    else:
        return f"{operation} is not a valid operation."

run = True
new_calculation = True
while run:
    if new_calculation:
        x = float(input("What's the first number?: "))
    print("+")
    print("-")
    print("/")
    print("*")
    operation = input("Pick an operation: ")
    y = float(input("What's the next number? "))
    answer = calc(x, y, operation)

    print(f"{x} {operation} {y} = {answer}")
    reuse_answer = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to quit: ")
    if reuse_answer == 'y':
        new_calculation = False
        x = answer
    elif reuse_answer == 'n':
        new_calculation = True
    elif reuse_answer == 'q':
        run = False
    else:
        print("Type 'y' or 'n' ")

