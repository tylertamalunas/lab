# need a singgle list of letters lowercase and capital, single list of symbols, random range for 0-9
import random

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
           'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

print("Welcome to the Password Generator.")
password_letters = int(input("How many letters would you like?\n"))
password_numbers = int(input("How many numbers?\n"))
password_symbols = int(input("How many symbols?\n"))

temp_password = []

for i in range(0, password_letters):
    temp_password.append(random.choice(letters))
for i in range(0, password_numbers):
    temp_password.append(random.choice(numbers))
for i in range(0, password_symbols):
    temp_password.append(random.choice(symbols))

random.shuffle(temp_password)
password = ''.join(temp_password) 
print(f"Your new password is: {password}")
