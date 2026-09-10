import random

print("Welcome to the PyPassword Generator!")

# Ask the user how many of each type they want
num_letters = int(input("\nHow many letters would you like in your password?\n"))
num_symbols = int(input("\nHow many symbols would you like?\n"))
num_numbers = int(input("\nHow many numbers would you like?\n"))

# Possible characters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 1. Create an empty LIST for the characters
password = []

# 2. Add random letters
for char in range(num_letters):
    password.append(random.choice(letters))

# 3. Add random symbols
for char in range(num_symbols):
    password.append(random.choice(symbols))

# 4. Add random numbers
for char in range(num_numbers):
    password.append(random.choice(numbers))

# At this point, it could look like:
# ['a', 'f', 'x', '#', '!', '7', '2']

# 5. Shuffle the list
random.shuffle(password)

# Now it could look like:
# ['7', 'a', '#', 'x', '2', 'f', '!']

# 6. Convert the list into a final string
final_password = ""

for char in password:
    final_password += char

# 7. Print it
print(f"\nYour password is: {final_password}")