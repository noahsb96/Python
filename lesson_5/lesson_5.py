# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
for x in range(1, nr_letters + 1):
    rand_letters = random.randint(0, len(letters))
    password.append(letters[rand_letters])
nr_symbols = int(input(f"How many symbols would you like?\n"))
for x in range(1, nr_symbols + 1):
    rand_symbols = random.randint(0, len(symbols))
    password.append(symbols[rand_symbols])
nr_numbers = int(input(f"How many numbers would you like?\n"))
for x in range(1, nr_numbers + 1):
    rand_numbers = random.randint(0, len(numbers))
    password.append(numbers[rand_numbers])
final = ''.join(password)
print(final)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(''.join(random.sample(final, len(final))))