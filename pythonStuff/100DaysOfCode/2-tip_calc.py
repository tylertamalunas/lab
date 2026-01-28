print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip % would you like to give? "))
people = int(input("How many people to split the bill? "))

tip = tip / 100
bill_with_tip = bill + (bill * tip)
split_bill = bill_with_tip / people

print(f"Each person should pay: ${split_bill:.2f}")
