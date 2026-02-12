def calc(x, y, operation):
    if operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    elif operation == '+':
        return x + y
    elif operation == '-'
        return x - y
    else:
        return f"{operation} is not a valid operation."

run = True
x = float(input("What's the first number?: "))
while run:
    print("+")
    print("-")
    print("/")
    print("*")
    operation = input("Pick an operation: ")
    y = float(input("What's the next number? "))
    answer = calc(x, y, operation)

    print(f"{x} {operation} {y} = {answer}")
    reuse_answer = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if reuse_answer == 'y':
            x = answer
        elif reuse_answer == 'n':
            run = False
        else:
            print("Type 'y' or 'n' ")

#TODO
"""
not finished, need to create function for while loop. 
    - One branch restarts with new numbers, other continues to use answer.
    - answer set to NONE initially?
    - reset to NONE whenever new calculation 
"""
