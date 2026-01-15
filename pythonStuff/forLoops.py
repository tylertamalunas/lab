num = int(input("Enter a number: "))
total = 0

for x in range(1, num + 1):
    print(x)
    total += x

print(f"Sum of all numbers from 1 to {num} is {total}")
