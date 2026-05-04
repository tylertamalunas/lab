# takes list of ints and returns 3 values: smallest, largest, average

def stats(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for num in numbers:
        total += num
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    average = format(float(total / len(numbers)), '.2f')
    return (smallest, largest, average)


run = True
numbers = []

while run:
    user_input = input("Enter a number or 'done': ")
    if user_input == 'done':
        run = False
        if len(numbers) < 1:
            print("List is empty")
        else:
            minimum, maximum, avg = stats(numbers)
            print(f"Min: {minimum}")
            print(f"Max: {maximum}")
            print(f"Average: {avg}")
    else:
        try:
            user_input = int(user_input)
            numbers.append(user_input)
        except ValueError:
            print("That is not a number.")

