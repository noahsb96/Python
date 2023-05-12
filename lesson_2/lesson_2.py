# # Data Types
# # String
# print("Hello"[4]) # Subscripting

# print("123" + "345") # Will not add mathematically like numbers. Will just concatenate to make 12345

# # Integer

# print(123 + 345) #This will add mathematically as they are integers

# 123_456_789 # underscores help visualize how big number is without using commas

# # Float

# 3.12159

# # Boolean

# True # Must have first letter capitalized
# False

# # len function does not work with integers

# # this function will not work and comes up with an error, can only concatenate str (not "int") to str, because we are trying to concatenate an integer
# num_char = len(input("What is your name?"))

# new_num_char = str(num_char) # changes integer to string

# print("Your name has " + new_num_char + " characters.")

# # print(type(num_char)) # checks data type

# a = float(123)
# print(70 + float("100.5")) # output is 170.5

# print(str(70) + str(100)) # output is 70100

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3 # always ends with a float
# 2**2 # exponent or 2 to the power of 2

# #PEMDAS

print(round(8 // 3)) # Floor division to create whole number instead of float

score = 0

score += 1 # manipulating score to add 1

print(score) 

height = 1.8
isWinning = True

#f-string makes it possible to put all data types in one string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
