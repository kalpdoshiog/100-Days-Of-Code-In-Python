import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
generated_password = []

for letters_in_list in range(nr_letters):
    random_letters = random.choice(letters)
    generated_password.append(random_letters)

for numbers_in_list in range(nr_numbers):
    random_numbers = random.choice(numbers)
    generated_password.append(random_numbers)

for symbols_in_list in range(nr_symbols):
    random_symbols = random.choice(symbols)
    generated_password.append(random_symbols)

print(generated_password)

# Hard Version
random.shuffle(generated_password)
print(generated_password)

gen_password_str = ""
for letter in generated_password:
    gen_password_str += letter

print(gen_password_str)
