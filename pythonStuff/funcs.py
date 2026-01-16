def is_even(num):
    return num % 2 == 0

inp = int(input("Enter a number: "))
if is_even(inp) == True:
    print(f"{inp} is even")
else:
    print(f"{inp} is odd")
