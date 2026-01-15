# GOAL: collect multiple values and work with them

numbers = []
for n in range(1, 6):
    inp = int(input(f"Enter number {n}: "))
    numbers.append(inp)
    
print(f"Numbers: {numbers}")
print(f"Smallest: {min(numbers)}")
print(f"Largest: {max(numbers)}")
