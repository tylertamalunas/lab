# repeatedly ask to enter numbers
# stops when "done" entered
# stores all valid numbers in a list
# once stopped, prints:
#   all numbers entered
#   count of numbers
#   average of numbers

run = True
num_list = []
total = 0
count = 0

while run:
    user_input = input("Enter a number or 'done' if finished: ")
    if user_input.lower() == "done":
        run = False
        print(f"Numbers: {num_list}")
        print(f"Count: {count}")
        print(f"Average: {float(total / count):.2f}")
    else:
        try:
            user_input = int(user_input)
            num_list.append(user_input)
            count += 1
            total += user_input
        except:
            print(f"{user_input} is not a number.")
