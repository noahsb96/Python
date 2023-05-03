import datetime
x = 2

# print(x)

x = 'This is a string!'

# print(x)

NUMBER_OF_DAYS_IN_A_WEEK = 7

# This will not work
# is_true = true

# This will work

is_true = True

# print(is_true)

# def my_function (num):
#     print(num)

# my_function(1)

# print(True and True)
# print(False or True)
# print(not True)

# print(2 == '2')

# print('string' + 1)

thing_to_do = 'Take it'
way_to_do_it = "easy"
pronoun = 'dude'

# print("{} {} {}. But {}!".format(thing_to_do, way_to_do_it, pronoun, thing_to_do))

# print("{0} {1} {2}. But {0}!".format(thing_to_do, way_to_do_it, pronoun))

# print(f"{thing_to_do} {way_to_do_it} {pronoun}. But {thing_to_do}!")

animals = ['lions', 'tigers', 'bears']
# print(animals[-1])

# print(len(animals))

animals.append('oh my')
# print(animals)
# animals.pop(-2)
animals.remove('lions')
print(animals)

secret_files = ["TOP SECRET", "ALSO TOP SECRET", "DON'T EVEN LOOK AT THIS"]

new_secret_files = ["PRETTY DARN SECRET", "WE SEEM NOT TO BE TRUSTED QUITE AS MUCH WITH TOP SECRET",
                    "MAYBE IT'S THAT WE LEAVE SECRETS IN ALL CAPS IN PLAIN TEXT"]

secret_files = secret_files + new_secret_files

# print(secret_files)

first_name = 'name'

student = {
    first_name: 'fred',
    4: 'this is a 4',
    'current_week': 4
}

# print(student.get('birthdate', 'unknown'))
# print(student.get('birthdate'))


if 'birthdate' in student:
    today = datetime.datetime.today()
    is_birthday = (student['birthdate'].month == today.month and student
                   ['birthdate'].day == today.day)

# student['age'] = 21

# print(student)

# del student['age']
if 'birthdate' in student:
    del student['birthdate']

# print(student)

# print(len(student))

x = -10

# if x < 0:
#     print('Negative')
# elif x == 0:
#     print('Zero')
# else:
#     print('Positive')

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# for i in range(len(animals)):
#     print(i)

# for animal in animals:
#     print(animal)
# else:
#     print('loop is done')

# for item in student.items():
#     print(item)


# where_are_my_things = {
#     'tarantula': 'bedside',
#     'underwear': 'dresser',
#     'pc': 'desk'
# }

# for item in where_are_my_things.items():
#     print(f'My {item[0]} is kept in the {item[1]}')

# def function_example(param_one, param_two):
#     """Example function returning string interpolation of parameters."""
#     interp = f'What a splendid function! I\'ve got my {param_one} and {param_two}'
#     return interp


# print(function_example('string 1', 'string 2'))

# print 1 - 99
# if num is divisible by 3 print fizz
# if num is divisible by 5 print buzz
# if num is divisible by 3 and 5 print fizzbuzz
# otherwise, just print the number

count = 0

for i in range(100):
    if not i % 3 and not i % 5:
        print('fizzbuzz')
    elif not i % 3:
        print('fizz')
    elif not i % 5:
        print('buzz')
    else:
        print(i)
