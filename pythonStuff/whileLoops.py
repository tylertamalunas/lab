# loops (while) and input validation

run = True
while run:
    num = int(input("Enter a number: "))
    if num > 10:
        print(f"{num} is greater than 10. Done")
        run = False
